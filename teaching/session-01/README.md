# Session 1 — Hello, web!

**Milestone:** Your planner **page is live** in the browser and a linked **JavaScript** file runs.

## What this folder contains

| File | Purpose |
|------|---------|
| `index.html` | Minimal page: title, one heading, link to CSS + JS |
| `css/style.css` | Bare-bones body font and spacing |
| `js/app.js` | Runs when the page loads and updates the heading |

## What to explain

1. **HTML = structure** — tags describe what is on the page (`<h1>`, `<p>`).
2. **CSS = style** — linked with `<link rel="stylesheet" href="css/style.css">`.
3. **JavaScript = behaviour** — linked with `<script src="js/app.js" defer>` so the HTML exists before the script runs.
4. **`DOMContentLoaded`** — safe moment to change the page after the browser has built the DOM.

## Try it

Open `index.html` in Chrome/Edge. You should see the heading change to *"My Study Planner is live!"*

## Next session (preview)

You will replace this single block with a **header**, **tasks**, and **notes** section (`session-02/`). Same file names; more HTML and CSS.

## Aligns with full app

Same `<script defer>` pattern as `../../index.html` (line 126). Session 1 in the full app is the hook at the top of `../../js/app.js`.
