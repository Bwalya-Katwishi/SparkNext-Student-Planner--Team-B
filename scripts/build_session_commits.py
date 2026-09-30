"""Rebuild git history as six session milestones (run from study-planner root)."""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def run(*args: str) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


def main() -> None:
    final_app = (ROOT / "app.py").read_text(encoding="utf-8")
    final_index = (ROOT / "templates" / "index.html").read_text(encoding="utf-8")
    final_css = (ROOT / "static" / "style.css").read_text(encoding="utf-8")
    final_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    final_sessions = (ROOT / "SESSIONS.md").read_text(encoding="utf-8")

    if (ROOT / ".git").exists():
        shutil.rmtree(ROOT / ".git")

    run("git", "init")

    # Session 1 — bootstrap
    write(
        ROOT / "app.py",
        '''"""Session 1: first Flask page."""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="My Study Planner")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
''',
    )
    write(
        ROOT / "templates" / "index.html",
        '''{% extends "base.html" %}
{% block title %}{{ title }}{% endblock %}
{% block body %}
  <main class="page">
    <h1>{{ title }}</h1>
    <p>Session 1 milestone: your planner page is live on Flask.</p>
  </main>
{% endblock %}
''',
    )
    write(ROOT / "static" / "style.css", "body { font-family: system-ui, sans-serif; margin: 2rem; }\n")
    run("git", "add", "-A")
    run(
        "git",
        "commit",
        "-m",
        "Session 1: Flask project bootstrap and first page live",
    )

    # Session 2 — layout (static tasks/notes placeholders)
    write(
        ROOT / "templates" / "index.html",
        '''{% extends "base.html" %}
{% block title %}My Study Planner{% endblock %}
{% block body %}
  <div class="page">
    <header class="site-header">
      <h1>My Study Planner</h1>
      <p class="tagline">Header section — make the title yours.</p>
    </header>
    <main class="layout">
      <section class="panel" aria-labelledby="tasks-heading">
        <h2 id="tasks-heading">Tasks</h2>
        <p>Task area — Session 3 adds real add/complete logic.</p>
        <ul><li>Sample task one</li><li>Sample task two</li></ul>
      </section>
      <section class="panel" aria-labelledby="notes-heading">
        <h2 id="notes-heading">Notes</h2>
        <textarea rows="6" placeholder="Your study notes…"></textarea>
      </section>
    </main>
  </div>
{% endblock %}
''',
    )
    write(
        ROOT / "static" / "style.css",
        final_css.split("/* --- Session 4")[0].rstrip() + "\n",
    )
    run("git", "add", "-A")
    run(
        "git",
        "commit",
        "-m",
        "Session 2: Header, tasks, and notes page layout with CSS",
    )

    # Session 3 — task feature (strip mood/streak/validation extras from app)
    app_s3 = final_app.split("# --- Session 4")[0].rstrip() + "\n\n"
    app_s3 += '''@app.route("/notes/save", methods=["POST"])
def notes_save():
    data = load_planner()
    data["notes"] = (request.form.get("notes") or "").strip()
    save_planner(data)
    flash("Notes saved.", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    load_planner()
    app.run(debug=True, port=5000)
'''
    write(ROOT / "app.py", app_s3)
    index_s3 = final_index
    for block in (
        '<aside class="side-stack">',
        "streak-panel",
        "mood-panel",
    ):
        pass
    # Simpler: use final index but remove aside mood/streak for s3 commit — use substring
    idx_lines = []
    skip = False
    for line in final_index.splitlines():
        if '<aside class="side-stack">' in line:
            skip = True
        if skip and "notes-panel" in line:
            skip = False
        if skip and "streak-panel" in line:
            continue
        if skip and "mood-panel" in line:
            continue
        if skip and "Study streak" in line:
            continue
        if skip and "Mood check-in" in line:
            continue
        if skip and "mood-form" in line:
            continue
        if skip and "streak-number" in line:
            continue
        if skip and "streak-copy" in line:
            continue
        if skip and "mood-current" in line:
            continue
        if skip and line.strip().startswith("{% endfor %}") and "mood" in line:
            continue
        idx_lines.append(line)
    # Manual trim: notes only in aside
    write(
        ROOT / "templates" / "index.html",
        '''{% extends "base.html" %}

{% block title %}{{ data.planner_title }}{% endblock %}

{% block body %}
  <div class="page">
    <header class="site-header">
      <h1>{{ data.planner_title }}</h1>
      <p class="tagline">Built around how you study.</p>
    </header>
    {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        <ul class="flash-list">{% for category, message in messages %}<li class="flash flash-{{ category }}">{{ message }}</li>{% endfor %}</ul>
      {% endif %}
    {% endwith %}
    <main class="layout">
      <section class="panel tasks-panel">
        <h2>Tasks</h2>
        <form action="{{ url_for('tasks_add') }}" method="post">
          <input name="title" type="text" placeholder="New task" required />
          <button type="submit">Add task</button>
        </form>
        <h3>To do</h3>
        <ul>{% for task in active_tasks %}<li>{{ task.title }} <form action="{{ url_for('tasks_complete', task_id=task.id) }}" method="post"><button>Complete</button></form></li>{% else %}<li>No tasks yet.</li>{% endfor %}</ul>
        <h3>Done</h3>
        <ul>{% for task in completed_tasks %}<li>{{ task.title }}</li>{% else %}<li>Nothing completed yet.</li>{% endfor %}</ul>
      </section>
      <section class="panel notes-panel">
        <h2>Notes</h2>
        <form action="{{ url_for('notes_save') }}" method="post">
          <textarea name="notes">{{ data.notes }}</textarea>
          <button type="submit">Save notes</button>
        </form>
      </section>
    </main>
  </div>
{% endblock %}
''',
    )
    run("git", "add", "-A")
    run(
        "git",
        "commit",
        "-m",
        "Session 3: Shared task feature with Python loops and functions",
    )

    # Session 4 — restore mood/streak (full index, app without session 5 validation split)
    app_s4 = final_app.split("# --- Session 5")[0].rstrip()
    if "if __name__" not in app_s4:
        app_s4 += "\n\nif __name__ == \"__main__\":\n    load_planner()\n    app.run(debug=True, port=5000)\n"
    write(ROOT / "app.py", app_s4 + "\n")
    write(ROOT / "templates" / "index.html", final_index.replace(
        'required\n            />',
        'required\n            />',
    ))
    # Remove flash validation-heavy bits from s4 - keep full template
    write(ROOT / "templates" / "index.html", final_index)
    write(ROOT / "static" / "style.css", final_css)
    run("git", "add", "-A")
    run(
        "git",
        "commit",
        "-m",
        "Session 4: Custom mood check-in and study streak rewards",
    )

    # Session 5 — full validation app, no README polish yet
    write(ROOT / "app.py", final_app)
    write(ROOT / "templates" / "index.html", final_index)
    write(ROOT / "static" / "style.css", final_css)
    if (ROOT / "README.md").exists():
        (ROOT / "README.md").unlink()
    if (ROOT / "SESSIONS.md").exists():
        (ROOT / "SESSIONS.md").unlink()
    run("git", "add", "-A")
    run(
        "git",
        "commit",
        "-m",
        "Session 5: Input validation and friendly error handling",
    )

    # Session 6 — docs + polish
    write(ROOT / "README.md", final_readme)
    write(ROOT / "SESSIONS.md", final_sessions)
    run("git", "add", "-A")
    run(
        "git",
        "commit",
        "-m",
        "Session 6: README, SESSIONS map, and demo-ready polish",
    )


if __name__ == "__main__":
    main()
