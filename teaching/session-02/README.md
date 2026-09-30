# Session 2 — Page skeleton + CSS

**Milestone:** The app **looks real**: header, **tasks** area, and **notes** area with spacing, colour, and layout.

## What this folder contains

Static HTML only — buttons and lists are **placeholders** (no JavaScript logic yet). That keeps the focus on structure and CSS.

| File | Purpose |
|------|---------|
| `index.html` | Header + tasks + notes sections (matches full app layout) |
| `css/style.css` | SparkNext brand theme (same as `../../css/style.css`) |
| `../../assets/sparknext-mark.svg` | Logo mark in the header lockup |

## What to explain

1. **Semantic sections** — `<header>`, `<main>`, `<section>`, `<aside>` help screen readers and your future self.
2. **CSS variables** (`:root`) — one place to change colours for the whole app.
3. **Grid layout** — `.layout` becomes two columns on wide screens (`@media`).
4. **Before / after** — screenshot plain HTML vs with `style.css` linked.

## Try it

Open `index.html`. Tasks are fake list items; notes do not save yet.

## Diff vs Session 1

- More HTML structure; linked stylesheet matches the **full** planner look.
- No `js/app.js` yet (behaviour comes in Session 3).

## Aligns with full app

Same section order and class names as `../../index.html` (header, tasks panel, notes panel). Mood/streak aside is added in Session 4.
