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

@app.route("/notes/save", methods=["POST"])
def notes_save():
    data = load_planner()
    data["notes"] = (request.form.get("notes") or "").strip()
    save_planner(data)
    flash("Notes saved.", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    load_planner()
    app.run(debug=True, port=5000)
