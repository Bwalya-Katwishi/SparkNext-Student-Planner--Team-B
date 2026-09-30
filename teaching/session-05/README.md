# Session 5 — Validation & error handling

**Milestone:** The app **handles edge cases** — empty tasks, bad task ids, over-long text, corrupt `localStorage` — with clear **flash messages** instead of breaking.

## What this folder contains

Session 4 features plus dedicated **validator functions** (same names as the full app):

| Function | Purpose |
|----------|---------|
| `validateTaskTitle` | Reject empty / too-long titles |
| `validateNotes` | Trim notes over 2000 chars |
| `validateMood` | Only allow listed moods |
| `parseTaskId` | Safe number parsing for Complete buttons |
| `loadPlanner` `try/catch` | Reset if JSON is corrupt |

## What to explain

1. **Validate early** — check input before changing data.
2. **`try/catch`** — `JSON.parse` throws on garbage; catch and recover.
3. **`flashMessages` + `showFlash`** — user-facing feedback without `alert()`.
4. **Test matrix** — empty add, complete twice, paste broken JSON in DevTools.

## Try it

In DevTools → Application → Local Storage, set `sFactorPlanner` to `{not valid json` and refresh — app should reset with an error flash.

## Diff vs Session 4

- Same HTML as full app (`index.html` matches `../../index.html` structure).
- `js/app.js` now matches **`../../js/app.js`** Session 5 behaviour (validators wired into forms).

## Aligns with full app

Compare side-by-side with `../../js/app.js` — Session 5 block and `loadPlanner` error path should match.
