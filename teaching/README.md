# Teaching snapshots (Team B mentors)

Each **`session-0N/`** folder is a **runnable checkpoint** mentees can open in the browser while you teach that week. The code is **not** the production app — it is a **step-by-step copy** that ends up matching the full planner in the parent folder (`../index.html`, `../css/`, `../js/`).

Visual design follows **SparkNext Learning Hub - Brand Guidelines.pdf** (colours, Merriweather + Inter, logo lockup). See `../BRAND.md`.

## How to use live

1. Open the session folder for **this week** (e.g. `session-03/`).
2. Double-click **`index.html`** (or serve the folder with a static server).
3. Read **`README.md`** in that folder for the milestone, talking points, and diff vs last week.
4. When mentees catch up, compare their work to **`../`** (the complete reference).

## Session map

| Folder | Milestone | Runs in browser? |
|--------|-----------|------------------|
| [session-01](session-01/README.md) | First HTML page + first script | Yes |
| [session-02](session-02/README.md) | Header, tasks, notes layout + CSS | Yes (static content) |
| [session-03](session-03/README.md) | Add / view / complete tasks + save notes | Yes |
| [session-04](session-04/README.md) | Mood check-in + study streak | Yes |
| [session-05](session-05/README.md) | Validation + error messages | Yes |
| [session-06](session-06/README.md) | Same as full app + polish checklist | Yes (= `../`) |

**Storage key:** all snapshots use `localStorage` key `sFactorPlanner` — reset in DevTools if a demo gets messy.

See **[ALIGNMENT.md](ALIGNMENT.md)** for a session-by-session diff vs the full app in `../`.
