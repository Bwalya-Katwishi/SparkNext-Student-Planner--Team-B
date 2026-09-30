# The [S] Factor — personalised study planner (reference)

Team B **Lead-Us Sessions** reference build using **HTML, CSS, and JavaScript** only. Styling follows **SparkNext brand guidelines** — see [BRAND.md](BRAND.md). Tasks and notes are saved in the browser with **localStorage** (they survive a refresh on the same device/browser).

## What it does

- **Tasks:** add, list, and complete study tasks (JavaScript arrays + functions, rendered with the DOM).
- **Notes:** free-text area saved in localStorage.
- **Make it yours:** daily mood check-in and a consecutive-day **study streak** when you complete tasks.
- **Validation:** friendly on-screen messages for empty tasks and bad saved data.

## Requirements

- A modern web browser (Chrome, Edge, Firefox, etc.)
- Optional: [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) in VS Code, or any static file server

## Run locally

**Easiest:** open `index.html` in your browser (double-click the file).

For closer-to-real-web practice, serve the folder:

```powershell
cd "c:\Users\bwaly\Desktop\SPARKNEXT PROJECT\study-planner"
python -m http.server 8080
```

Then open [http://localhost:8080](http://localhost:8080).

To reset all data: DevTools → Application → Local Storage → delete `sFactorPlanner`, or run in the console: `localStorage.removeItem('sFactorPlanner')`.

## Project layout

```
study-planner/
  index.html          # Page structure (Session 2 layout)
  css/style.css       # Layout and theme
  js/app.js           # Logic, storage, validation (Sessions 3–5)
  teaching/           # Per-session code + README for live teaching
    session-01/ … session-06/
  SESSIONS.md         # Week-by-week teaching map
```

## Teaching

See **SESSIONS.md** for which files to open in each Friday session.
