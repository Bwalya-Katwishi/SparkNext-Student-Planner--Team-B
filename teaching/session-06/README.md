# Session 6 — Polish & handoff

**Milestone:** **Demo-ready** planner — same code as the **full reference** in the parent folder, plus a short polish checklist for Spark Tank / graduation.

## What this folder contains

This snapshot is **intended to match** the complete app:

| File | Same as |
|------|---------|
| `index.html` | `../../index.html` |
| `js/app.js` | `../../js/app.js` |
| `css/style.css` | `../../css/style.css` |

If anything drifts, **`../../`** is the source of truth — update this folder to match before teaching.

## Polish checklist (mentees)

- [ ] Planner title and copy sound like *you* (not default placeholder text).
- [ ] No `console.log` debug left in `app.js`.
- [ ] Empty states read kindly (`No open tasks…`).
- [ ] Test: add task → refresh → complete → mood → corrupt storage recovery (Session 5).
- [ ] README in project root explains how to run (`../../README.md`).
- [ ] One screenshot or short screen recording for your portfolio.

## What to explain

1. **Refactoring** — validators and render live in named functions (easier to demo one line in Spark Tank).
2. **Accessibility** — labels, `aria-labelledby`, skip link (point at `index.html`).
3. **What you learned / what was hard** — exit ticket for the cohort.

## Try it

Open `index.html` — behaviour should be identical to opening `../../index.html`.

## Teaching note

Earlier weeks live in `../session-01/` … `../session-05/`. Use those for *building*; use **`../../`** or this folder for the *final* comparison.
