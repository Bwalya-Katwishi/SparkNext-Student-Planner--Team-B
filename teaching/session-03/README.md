# Session 3 — Shared task feature (JavaScript)

**Milestone:** **Add**, **view**, and **complete** tasks using **arrays**, **loops**, and **functions** — lists are drawn with JavaScript, not hard-coded in HTML. Notes and title **save** via `localStorage`.

## What this folder contains

| File | Purpose |
|------|---------|
| `index.html` | Same task + notes layout as the full app (no mood/streak yet) |
| `js/app.js` | `loadPlanner` / `savePlanner`, `addTask`, `render`, form handlers |
| `css/style.css` | Same as full app |

## What to explain

1. **`localStorage`** — JSON string in the browser; survives refresh (show in DevTools → Application).
2. **`tasks` array** — each task is an object `{ id, title, done, created }`.
3. **`for` loops** — `activeTasks` / `completedTasks` filter what to show.
4. **DOM** — `render()` clears lists and rebuilds `<li>` elements from data (not copy-paste HTML per task).
5. **`preventDefault()`** — stops forms from reloading the page.

## Try it

Add tasks, complete one, refresh — data should remain. Open DevTools and inspect key `sFactorPlanner`.

## Diff vs Session 2

- Enabled forms; dynamic task lists replace static samples.
- Still **no** mood/streak panels (Session 4) and **minimal** error checks (Session 5 adds `validateTaskTitle`, etc.).

## Aligns with full app

Same functions and IDs as `../../js/app.js` Session 3 block. `completeTask` here does **not** call `updateStudyStreak` yet (that is Session 4).
