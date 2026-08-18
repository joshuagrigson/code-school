# Code School — `code-lab.html`

The complete Kindergarten-through-College coding class in one self-contained,
offline HTML file. Download it (or copy it to `C:\code-school\`), double-click,
and it runs in any browser with **zero network access and zero API usage**.

## What's inside — 57 lessons, 14 grades

| Grades | Territory |
|---|---|
| K–1 | HTML: tags, attributes, lists, buttons, links, boxes |
| 2–3 | CSS: colors, spacing, borders, classes and ids |
| 4–6 | JavaScript: `screen.textContent`, variables, strings vs numbers, lists, random |
| 7 | Functions — teach, ingredients, `return`, functions calling functions (4 lessons) |
| 8 | Choices — if, else, else-if chains, `&&`/`\|\|` (4 lessons) |
| 9 | Loops — for, for...of, nesting, while (4 lessons) |
| 10 | Build the Excuse-O-Matic in three staged sittings (3 lessons) |
| 11 | Objects — labels, dot access, lists of objects, changing state (4 lessons) |
| 12 | Debugging — console.log, reading errors, typeof, guarding input (4 lessons) |
| College | Naming, one-job functions, DRY, the Mood Machine final project, graduation (5 lessons) |

Lesson indices 0–28 match the original build exactly, and the `CARRIED` seed
preserves Josh's progress (28/57, resuming at "Picking at random") in any fresh
browser. Real progress lives in `localStorage` under `codeschool` and always
wins over the seed.

## Features

- Live preview on every keystroke; JS lessons enforce the house rule —
  *working it out is not showing it* — via the universal `.textContent =` check
  plus a `new Function` syntax gate with friendly error rewrites.
- **Give me a lead** reveals the answer in 4 word-snapped steps (scaffold, don't solve).
- **Ask a question**: offline keyword-matched answer bank (32 entries).
- **Free play** sandbox (self-saving, uncheckable, unbreakable).
- Per-grade redo buttons, REMEMBER strip per language, reading level that
  "ages up" with the grades.

After College graduation, the next step is the [12-week Paper Plate course](../course/README.md)
in this repo — servers, Git, deployment, AI APIs, and shipping real features.

## For maintainers

The parser traps from the original build still apply: the inline script must
never contain the literal sequences for a closing body tag, an HTML comment
opener, or script open/close tags — they are built via string concatenation or
escaped (`safeJs`, `'<scr'+'ipt>'`). Test with the recipe in the original
HANDOFF: serve locally, click every lesson's "Show me" (all must pass) and
"Start over" (none may pass), and verify stripped-output solutions fail.
