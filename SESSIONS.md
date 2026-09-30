# The [S] Factor — session map (Team B study planner)

This reference app is **one complete codebase**; comments and git history are labelled so mentors can jump to the right week in a live session.

| Session | Milestone (teaching focus) | What changed | Point mentees here |
|--------|----------------------------|--------------|-------------------|
| **1** | Environment ready + first Flask page live | `requirements.txt`, Flask app bootstrap, `templates/base.html`, first route | `app.py` (Session 1 block), run `python app.py` |
| **2** | Page layout: **header**, **tasks**, **notes** | `templates/index.html` structure, `static/style.css` layout/colour | `index.html` header + sections, `style.css` Session 2 block |
| **3** | **Shared feature:** add / view / complete tasks with Python | `add_task`, `active_tasks`, POST routes, Jinja `for` loops | `app.py` Session 3, task form + lists in `index.html` |
| **4** | **Make it yours:** mood check-in + study **streak** | `update_study_streak`, mood route, streak/mood panels | `app.py` Session 4, aside panels in `index.html` |
| **5** | **Validation & errors** — empty input, bad ids, corrupt file | `validate_*`, `flash` messages, safe JSON load | `app.py` Session 5, flash list in `index.html` |
| **6** | **Polish & handoff** — README, naming, demo-ready run | `README.md`, this file, footer copy, no debug clutter | `README.md`, `if __name__ == "__main__"` block |

## Facilitation notes (from Web Makers — *how*, not *what*)

- **Small steps:** show one route or one template section at a time; run the app after each change.
- **PRIMM:** predict what a form will do → run it → inspect `data/planner.json` together.
- **Pair programming:** one person reads `app.py`, one person edits HTML; swap for Session 3 routes.

## Primary curriculum doc

The **Team B Guide** should be the source of truth for exact milestone wording. If your copy differs from this table, follow the guide and treat this repo as the technical reference implementation.
