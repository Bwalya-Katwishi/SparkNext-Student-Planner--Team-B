# The [S] Factor — personalised study planner (reference)

Team B **Lead-Us Sessions** reference build: HTML + CSS front end, **Flask** back end, JSON file storage. Mentees are meant to follow the same shape in their own repos.

## What it does

- **Tasks:** add, list, and complete study tasks (Python lists + functions, not hard-coded HTML).
- **Notes:** free-text area saved on the server.
- **Make it yours:** daily mood check-in and a consecutive-day **study streak** when you complete tasks.
- **Validation:** friendly error messages for empty tasks, bad links, and broken data files.

## Requirements

- Python 3.10+ (3.10 is fine on Windows)
- pip

## Run locally

```powershell
cd "c:\Users\bwaly\Desktop\SPARKNEXT PROJECT\study-planner"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

Saved data lives in `data/planner.json` (created on first run). Delete that file to reset.

## Project layout

```
study-planner/
  app.py              # Flask routes and Python logic (see Session comments)
  requirements.txt
  templates/          # HTML (Jinja)
  static/style.css    # Layout and theme
  data/               # planner.json at runtime
  SESSIONS.md         # Week-by-week teaching map
```

## Teaching

See **SESSIONS.md** for which files to open in each Friday session.
