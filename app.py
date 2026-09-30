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

if __name__ == "__main__":
    load_planner()
    app.run(debug=True, port=5000)

