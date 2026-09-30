"""
The [S] Factor — personalised study planner (Team B reference app).

Run locally: python app.py
"""

from __future__ import annotations

import json
from datetime import date, datetime
from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, url_for

# --- Session 1: project bootstrap & first page ---
APP_ROOT = Path(__file__).resolve().parent
DATA_FILE = APP_ROOT / "data" / "planner.json"

app = Flask(__name__)
# Flash messages need a secret key so Flask can sign session cookies safely.
app.secret_key = "s-factor-dev-key-change-me"


def default_planner_data() -> dict:
    """Starting data when someone runs the app for the first time."""
    return {
        "planner_title": "My Study Planner",
        "study_style_note": "",
        "notes": "",
        "tasks": [],
        "next_task_id": 1,
        "mood_today": "",
        "streak_days": 0,
        "last_streak_date": "",
    }


def load_planner() -> dict:
    """Read planner data from disk (or create a fresh file)."""
    if not DATA_FILE.exists():
        data = default_planner_data()
        save_planner(data)
        return data

    try:
        with DATA_FILE.open(encoding="utf-8") as handle:
            data = json.load(handle)
    except (json.JSONDecodeError, OSError):
        # --- Session 5: survive bad/corrupt data files ---
        flash("Your saved data looked broken — we started a fresh planner.", "error")
        data = default_planner_data()
        save_planner(data)
        return data

    # Merge missing keys if we add features later (keeps old files working).
    base = default_planner_data()
    for key, value in base.items():
        data.setdefault(key, value)
    return data


def save_planner(data: dict) -> None:
    """Write planner data so tasks survive closing the browser."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2)


# --- Session 3: shared task feature (Python logic, not hard-coded HTML) ---


def find_task(data: dict, task_id: int) -> dict | None:
    """Return one task dict by id, or None if it does not exist."""
    for task in data["tasks"]:
        if task["id"] == task_id:
            return task
    return None


def add_task(data: dict, title: str) -> None:
    """Append a new task using a loop-friendly list structure."""
    task = {
        "id": data["next_task_id"],
        "title": title,
        "done": False,
        "created": date.today().isoformat(),
    }
    data["tasks"].append(task)
    data["next_task_id"] += 1


def complete_task(data: dict, task_id: int) -> bool:
    """Mark a task done. Returns False if the id was invalid."""
    task = find_task(data, task_id)
    if task is None:
        return False
    if not task["done"]:
        task["done"] = True
        # --- Session 4: custom feature (study streak) ---
        update_study_streak(data)
    return True


def active_tasks(data: dict) -> list[dict]:
    """Tasks still to do — mentors can point to this loop in templates."""
    return [task for task in data["tasks"] if not task["done"]]


def completed_tasks(data: dict) -> list[dict]:
    return [task for task in data["tasks"] if task["done"]]


# --- Session 4: custom feature (mood + streak) ---

ALLOWED_MOODS = ("focused", "tired", "stressed", "motivated", "calm")


def update_study_streak(data: dict) -> None:
    """
    Increase streak when you complete at least one task on consecutive days.
    We store the last date as text (YYYY-MM-DD) so JSON stays simple.
    """
    today = date.today().isoformat()
    last = data.get("last_streak_date") or ""

    if last == today:
        return

    if last == "":
        data["streak_days"] = 1
    else:
        try:
            last_day = date.fromisoformat(last)
            gap = (date.today() - last_day).days
        except ValueError:
            gap = 999

        if gap == 1:
            data["streak_days"] = int(data.get("streak_days", 0)) + 1
        elif gap > 1:
            data["streak_days"] = 1
        else:
            data["streak_days"] = max(int(data.get("streak_days", 0)), 1)

    data["last_streak_date"] = today


def streak_message(streak_days: int) -> str:
    """Small reward copy — mentees can swap this for their own voice."""
    if streak_days <= 0:
        return "Complete a task today to start your streak."
    if streak_days == 1:
        return "Day 1 — nice start. Keep showing up."
    return f"{streak_days}-day streak! You are building a real habit."


# --- Session 5: input validation & error handling ---


def validate_task_title(raw_title: str) -> tuple[str | None, str | None]:
    """Return (clean_title, error_message). None title means invalid."""
    title = (raw_title or "").strip()
    if not title:
        return None, "Task title cannot be empty."
    if len(title) > 120:
        return None, "Task title is too long (max 120 characters)."
    return title, None


def validate_notes(raw_notes: str) -> tuple[str, str | None]:
    notes = (raw_notes or "").strip()
    if len(notes) > 2000:
        return notes[:2000], "Notes trimmed to 2000 characters."
    return notes, None


def validate_mood(raw_mood: str) -> tuple[str | None, str | None]:
    mood = (raw_mood or "").strip().lower()
    if not mood:
        return None, None
    if mood not in ALLOWED_MOODS:
        return None, "Please pick a mood from the list."
    return mood, None


def parse_task_id(raw_id: str) -> tuple[int | None, str | None]:
    try:
        task_id = int(raw_id)
    except (TypeError, ValueError):
        return None, "That task link was invalid."
    if task_id < 1:
        return None, "That task link was invalid."
    return task_id, None


@app.route("/", methods=["GET"])
def index():
    data = load_planner()
    return render_template(
        "index.html",
        data=data,
        active_tasks=active_tasks(data),
        completed_tasks=completed_tasks(data),
        moods=ALLOWED_MOODS,
        streak_message=streak_message(int(data.get("streak_days", 0))),
    )


@app.route("/tasks/add", methods=["POST"])
def tasks_add():
    data = load_planner()
    title, error = validate_task_title(request.form.get("title"))
    if error:
        flash(error, "error")
        return redirect(url_for("index"))

    add_task(data, title)
    save_planner(data)
    flash("Task added.", "success")
    return redirect(url_for("index"))


@app.route("/tasks/<task_id>/complete", methods=["POST"])
def tasks_complete(task_id: str):
    data = load_planner()
    parsed_id, error = parse_task_id(task_id)
    if error:
        flash(error, "error")
        return redirect(url_for("index"))

    ok = complete_task(data, parsed_id)
    if not ok:
        flash("That task no longer exists.", "error")
        return redirect(url_for("index"))

    save_planner(data)
    flash("Task completed — streak updated if today is a new day.", "success")
    return redirect(url_for("index"))


@app.route("/notes/save", methods=["POST"])
def notes_save():
    data = load_planner()
    notes, warn = validate_notes(request.form.get("notes"))
    data["notes"] = notes
    save_planner(data)
    if warn:
        flash(warn, "error")
    else:
        flash("Notes saved.", "success")
    return redirect(url_for("index"))


@app.route("/mood/set", methods=["POST"])
def mood_set():
    data = load_planner()
    mood, error = validate_mood(request.form.get("mood"))
    if error:
        flash(error, "error")
        return redirect(url_for("index"))
    data["mood_today"] = mood or ""
    save_planner(data)
    if mood:
        flash(f"Mood logged: {mood}.", "success")
    else:
        flash("Mood cleared.", "success")
    return redirect(url_for("index"))


@app.route("/planner/title", methods=["POST"])
def planner_title_save():
    data = load_planner()
    title = (request.form.get("planner_title") or "").strip()
    if not title:
        flash("Planner title cannot be empty.", "error")
        return redirect(url_for("index"))
    if len(title) > 80:
        title = title[:80]
        flash("Title trimmed to 80 characters.", "error")
    data["planner_title"] = title
    save_planner(data)
    flash("Planner title updated.", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    # --- Session 6: tidy entry point for demos ---
    load_planner()
    app.run(debug=True, port=5000)
