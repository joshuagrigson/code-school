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

## Ways of teaching that are not reading

Every lesson is still "read a little, type the real thing". Around that core,
the school borrows the mechanics that make Duolingo, Brilliant, Tynker, Hedy,
Grasshopper, Khan Academy and PRIMM-style classrooms work, all offline and all
keyed to the lesson they belong to. None of them can be pasted into the editor;
they exist so the typing lands on an idea that already clicked.

| Mechanic | Borrowed from | What the learner does |
|---|---|---|
| 🔮 **Before it runs** (`PRED`) | Brilliant, PRIMM *Predict* | Commit to a guess about the output, then see it settle. |
| 🎛 **Try it** (`TRYIT`) | Brilliant manipulables | Drag a knob / tap a swatch; code and page change together. |
| 🧩 **Warm-up** (`SHUF`) | Parsons problems | Put the answer's scrambled lines in working order. |
| 🔍 **The glass machine** (`TRACE`) | PRIMM *Investigate*, tracing tables | Step a loop one lap at a time and watch every box. |
| 🖼 **In one picture** (`PICS`) | dual coding (Brilliant, Khan) | One diagram per big idea: the hug, the box, the machine, the fork, the lap, the drawers. |
| 🧩 **Build the line** (`TILES`) | Duolingo word tiles, Tynker block→text | Tap tiles to assemble one line of code; two tiles are decoys. |
| ✎ **Fill the gap** (`CLOZE`) | Hedy's pink blank, Grasshopper | One piece of real code is missing; tap the piece that fits. |
| 🐛 **Spot the bug** (`BUGS`) | PRIMM *Investigate*, "errors are the curriculum" | One line is wrong; find it before the computer does, then read the fix. |
| 🧠 **Quick recall** (`RECALL`) | Duolingo spaced repetition + mistake review | One question from an *earlier* lesson at the top of the page. Right answers push it further out; a miss brings it back next lesson with a "revisit" link. |
| 🌀 **One more twist** (`TWIST`) | PRIMM *Modify*, Brilliant "play with it" | After the tick, one small change to make to your own working code. |
| 👣 **The footpath** | Khan talk-through ordering | Chips walk the learner through the page's stations in order, ending at the editor. |
| 👻 **The ghost coach** | worked-example fading | A guided lap where the next word types itself faintly, then a solo lap for the tick. |
| 🦆 **The duck** | rubber-duck debugging | Explain your own code aloud, one line at a time. |

Warm-ups (tiles, gap, bug, scrambled lines) disappear once a lesson is ticked;
the picture and the recall card stay. Recall progress lives in `localStorage`
under `recall`, the other mechanics' XP under `teach2`.

After College graduation the course sends learners off to build a small real project of their own — the school is deliberately self-contained.

## For maintainers

The parser traps from the original build still apply: the inline script must
never contain the literal sequences for a closing body tag, an HTML comment
opener, or script open/close tags — they are built via string concatenation or
escaped (`safeJs`, `'<scr'+'ipt>'`). Test with the recipe in the original
HANDOFF: serve locally, click every lesson's "Show me" (all must pass) and
"Start over" (none may pass), and verify stripped-output solutions fail.

Per-lesson extras (`PRED`, `TRYIT`, `SHUF`, `TRACE`, `PICS`, `TILES`, `CLOZE`,
`BUGS`, `RECALL`, `TWIST`, plus `RN`, `MORE`, `OLDS`, `RW`) are keyed by lesson
index. Append new lessons at the end of their grade block rather than inserting
mid-array, or every downstream index shifts. `TWIST` checks must be satisfiable
while the lesson's own check still passes (ask for additions, not swaps).

## For skeptics

If you're a working developer looking at the kindergarten vocabulary and the
confetti and thinking "these kids and their shortcuts" — this section is for you.

**The pedagogy, straight:**

- **Everything is typed by hand.** No copy-paste, no autocomplete, no AI at
  runtime. The file makes zero network calls; a learner cannot outsource the
  typing that builds the skill.
- **Errors are the curriculum.** A syntax gate (`new Function` parse) blocks
  green ticks on broken code; a structural linter explains unclosed tags,
  blocks-inside-paragraphs, and empty CSS values in plain English instead of
  letting browser error-recovery hide them. Learners are deliberately made to
  cause and read errors.
- **The kid-terms are scaffolding with a demolition date.** Every "hug/box/trick"
  lesson carries a *Real name* panel (element/tag, variable, function, parameter,
  return value, conditional, iteration, state, property). Graduates exit
  speaking standard vocabulary.
- **No magic survives to graduation.** The pre-wired `screen`/`btn` handles are
  revealed as `document.getElementById` in Grade 12 — and learners write the
  real version. The checker itself is disclosed as plain JavaScript. Free play
  invites them to view-source the whole school.
- **Simplifications are labeled.** Where the material simplifies (browser error
  recovery, zero-indexing, pseudo-randomness), a collapsible "the full truth"
  note says so and states the precise version.
- **Reviews are placement exams.** Every grade ends with a cumulative review;
  passing one *first* test-outs the whole grade (marked ⚡). Experienced learners
  fast-forward to their actual gaps; beginners get consolidation checkpoints.
- **Restraint on gamification.** XP, confetti and a gentle daily streak
  celebrate; there are no timers, lives, hearts, or leaderboards. Motivation
  without engagement-farming.

**The audit invitation:** it's one dependency-free HTML file. Open it. Read the
checker (`runCheck`), the linter (`htmlLint`), the highlighter, the lesson data.
Then judge. Issues and pull requests welcome.
