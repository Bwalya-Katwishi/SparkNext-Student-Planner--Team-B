# The [S] Factor — session map (Team B study planner)

This reference app uses **HTML, CSS, and JavaScript** only. Comments in the code are labelled so mentors can jump to the right week in a live session.

**Mentor teaching snapshots:** each week has a runnable mini-copy with explanations in [`teaching/session-01/`](teaching/session-01/README.md) … [`teaching/session-06/`](teaching/session-06/README.md). See [`teaching/README.md`](teaching/README.md) for the overview.

| Session | Milestone (teaching focus) | What changed | Point mentees here |
|--------|----------------------------|--------------|-------------------|
| **1** | First page live in the browser | `index.html` skeleton, link to `js/app.js`, open file in browser | `index.html` bottom `<script>`, `js/app.js` Session 1 block |
| **2** | Page layout: **header**, **tasks**, **notes** | `index.html` sections, `css/style.css` layout/colour | Header + main grid in `index.html`, `style.css` Session 2 block |
| **3** | **Shared feature:** add / view / complete tasks with JS | `loadPlanner`, `addTask`, DOM `render`, event listeners | `js/app.js` Session 3, task form in `index.html` |
| **4** | **Make it yours:** mood check-in + study **streak** | `updateStudyStreak`, mood form, streak panel | `js/app.js` Session 4, aside panels in `index.html` |
| **5** | **Validation & errors** — empty input, corrupt storage | `validate_*`, flash messages, `try/catch` on JSON | `js/app.js` Session 5, `#flash-list` in `index.html` |
| **6** | **Polish & handoff** — README, naming, demo-ready | `README.md`, this file, tidy init in `app.js` | `README.md`, `DOMContentLoaded` at bottom of `js/app.js` |

## Facilitation notes (from Web Makers — *how*, not *what*)

- **Small steps:** change one function or one CSS block, refresh the browser, show the result.
- **PRIMM:** predict what Add task will do → click it → open DevTools → Application → Local Storage → inspect `sFactorPlanner`.
- **Pair programming:** one person reads `app.js`, one person edits HTML/CSS; swap for Session 3.

## Primary curriculum doc

The **Team B Guide** should be the source of truth for exact milestone wording. If your copy differs from this table, follow the guide and treat this repo as the technical reference implementation.
