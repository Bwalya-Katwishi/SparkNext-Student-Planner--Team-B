# Teaching snapshots ↔ full app

The **complete reference** lives one level up: `../index.html`, `../css/style.css`, `../js/app.js`.

Each `session-0N/` folder is a **checkpoint** mentees build toward that reference. Use this table when prepping or diffing in class.

| Session | Folder | Same as full app? | Main gap vs `../` |
|--------|--------|-------------------|-------------------|
| 1 | `session-01/` | No | Minimal HTML/CSS; one-line JS only |
| 2 | `session-02/` | Layout only | Static tasks/notes; no `js/app.js` |
| 3 | `session-03/` | Partial | Tasks + notes + title; **no** mood/streak HTML or JS |
| 4 | `session-04/` | Partial | Mood + streak; validators still inline (not `validate_*`) |
| 5 | `session-05/` | Logic yes | `app.js` matches `../js/app.js`; HTML eyebrow text differs |
| 6 | `session-06/` | **Yes** | Should match `../` — re-copy if anything drifts |

## Shared details (all sessions that use storage)

- **localStorage key:** `sFactorPlanner` (same as full app — clear between demos if needed).
- **CSS:** from Session 2 onward, `css/style.css` matches `../css/style.css`.
- **IDs / forms:** Session 3+ use the same element IDs as the full app so mentees can paste into `../` incrementally.

## Suggested live flow

1. Teach from `session-0N/README.md` talking points.
2. Show runnable `session-0N/index.html`.
3. Optional: diff `session-0N/js/app.js` against `session-0(N-1)/js/app.js` or against `../js/app.js`.
