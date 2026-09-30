# SparkNext brand — study planner implementation

This app follows **SparkNext Learning Hub - Brand Guidelines.pdf** (project root).

## Official palette (digital UI)

| Token | Hex | Use in this app |
|-------|-----|-----------------|
| Navy (primary dark) | `#1A4149` | Header background, primary buttons, headings |
| Forest green | `#0A261A` | Hover states, success text |
| Deep neutral | `#2E170E` | Error text |
| Mint | `#8FBE9E` | Borders, accents, task chips |
| Olive | `#B5BE62` | Secondary buttons |
| Cream | `#FFF5D2` | Header text, page gradient base |
| Gold | `#FAD465` | Eyebrows, streak highlight, focus rings |
| White | `#FFFFFF` | Cards / panels |

Pairing follows the guideline **Color Palette Pairs** slide (e.g. navy + cream, navy + gold, mint + navy).

## Typography (web / Google Docs slide)

- **Headings (planner title, streak number):** [Merriweather](https://fonts.google.com/specimen/Merriweather), regular weight for main title (not bold per docs).
- **UI & body:** [Inter](https://fonts.google.com/specimen/Inter); subheadings bold.
- **Wordmark:** “SparkNext” = serif; “Learning Hub” = sans-serif bold uppercase (logo guidelines).

## Logo

- Mark SVG: `assets/sparknext-mark.svg` (single colour via `currentColor` — do not recolour icon and wordmark differently on the lockup).
- Do **not** set the brand name “SparkNext” in Montserrat/Inter; use Merriweather in the lockup only.

## Voice (microcopy)

Professional, friendly, resourceful — aligned with **Voice & Tone** (page 05): encourage mentees without corporate jargon.

## Teaching folder

Session snapshots use the same `css/style.css` tokens and the same header lockup paths (`../../assets/` from `teaching/session-NN/`).
