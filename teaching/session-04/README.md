# Session 4 — Make it yours (mood + streak)

**Milestone:** A **personal** layer on top of the shared task feature: **mood check-in** and a **study streak** when you complete tasks on consecutive days.

## What this folder contains

Everything from Session 3, plus:

| Addition | File |
|----------|------|
| Streak + mood panels in HTML | `index.html` (`aside` sections) |
| `updateStudyStreak`, mood save, streak copy | `js/app.js` Session 4 block |

## What to explain

1. **Streak logic** — compare today's date (`YYYY-MM-DD`) with `last_streak_date`; gap of 1 day increments streak, bigger gap resets to 1.
2. **Why mood?** — helps mentees notice *how* study feels, not just *what* they did.
3. **`completeTask` now calls `updateStudyStreak`** — tie habit tracking to an action they already understand.

## Try it

Complete a task → streak shows 1 day. Change mood → refresh → mood persists. (Use DevTools to tweak `last_streak_date` in `localStorage` for a demo of multi-day streaks.)

## Diff vs Session 3

- New HTML in the aside stack (matches `../../index.html`).
- Streak does not yet use dedicated **`validate_*`** helpers (Session 5).

## Aligns with full app

Same streak/mood behaviour as `../../js/app.js` Session 4. Validation is still inline/simple until Session 5.
