# Code School — `code-lab.html`

> **Want to understand what you just created, past vibe-coding? Want full
> control over AI-assisted creations? #Code-School**

The complete Kindergarten-through-College coding class in one self-contained,
offline HTML file. Download it (or copy it to `C:\code-school\`), double-click,
and it runs in any browser with **zero network access and zero API usage**.

## What's inside — 143 lessons

Graduation is the 107 required lessons — every lesson and every practice rep.
Challenges, portfolio pieces, Beyond and the Review Desk sit outside that count.

| Track | Territory |
|---|---|
| K–1 | HTML: tags, attributes, lists, buttons, links, boxes |
| 2–3 | CSS: colours, spacing, borders, classes and ids |
| 4–6 | JavaScript: `screen.textContent`, variables, strings vs numbers, lists, random |
| 7 | Functions — teach, ingredients, `return`, functions calling functions |
| 8 | Choices — if, else, else-if chains, `&&` / `\|\|` |
| 9 | Loops — for, for...of, building in a loop, while |
| 10 | Build the Excuse-O-Matic in three staged sittings |
| 11 | Objects — labels, dot access, lists of objects, changing state |
| 12 | Debugging — console.log, reading errors, typeof, guarding input |
| College | Naming, one-job functions, DRY, the Mood Machine, graduation |
| Hustle | Turning code into money: a marketing page, a call to action, an app on a phone |
| Machine Room | Why one way beats another: counting work, search, hashing, sorting, Big-O |
| Portfolio | Five client jobs graded by a sign-off checklist, unlocked by the grades they need |
| **Beyond** | **15 lessons after graduation: reading and fixing code you did not write, verifying what a machine wrote, writing a spec, asking a question that gets answered, commit messages, READMEs, shipping, secrets, untrusted input, accessibility, transferring to the next language, and performance** |
| **Review Desk** | **10 lessons on reading code a machine wrote — see below** |

Reviews double as test-out exams (⚡): pass one first and it ticks the whole
grade. Challenges are hint-free. Reps (🏋) are required: they count toward the
grade and toward graduation, because the practice most likely to make something
stick was the practice easiest to skip. Beyond and the Review Desk sit outside
the graduation count on purpose — they are what you do after finishing, not a
moved goalpost.

## The Review Desk: reading code a machine wrote

Generating code is easy now. Reading it is the skill that decides whether you
own what you shipped or merely possess it. Every lesson in this track is a
**review**, not a build: a generated draft arrives, and the learner reads it
before running it, then decides whether to keep it, fix it, or bin it.

| # | The draft | What it teaches |
|---|---|---|
| 1 | Sums `qty` where the name promises money | The name and the code disagree, and nothing will tell you |
| 2 | Calls `list.max()` | An invented method — the loud failure |
| 3 | `average([])` returns `NaN` | The edge case the request never mentioned |
| 4 | A greeting with a settings object and a shouting flag | Cutting what nobody asked for |
| 5 | A missing price comes back as `0` | Sentinel values, and the truthiness trap that hides free water |
| 6 | A visitor's comment reaches `innerHTML` two functions away | Following untrusted text to its sink |
| 7 | Two drafts pasted in, one unreachable | Dead code and an orphan with a different boundary |
| 8 | `getUserName` also stamps `lastSeen` | The hidden side effect |
| 9 | Uses `TAX_RATE` and `formatMoney`, neither of which exists | Code written for somebody else's repository |
| 10 | `isEven` by checking the last digit against a list | Being willing to bin the whole draft |

The hint buttons are still there, but the worked-example ghost coach is not:
Beyond and the Review Desk are reading-and-deciding work, and a coach that fades
in the answer one word at a time does the deciding for you.

Every editor theme is available from the first minute of Kindergarten. Making a
learner earn a colour scheme gates comfort, not difficulty, and the person most
likely to need the light or high-contrast theme is the beginner who has not
earned anything yet.

Real progress lives in `localStorage` under `codeschool`, with the review
schedule under `srs`. A save code carries all of it to another device.

## The hub: never having to decide what to do next

A returning learner lands on one screen with one big button and the reason
underneath it. Mistakes outrank review, review outranks the next lesson, and it
falls through to challenges, portfolio pieces and free play. It is skippable for
anyone who would rather be dropped straight into the lesson, and `Ctrl`+`K`
jumps to any lesson or action from anywhere.

- **The memory engine.** Every question the school can ask — recall cards,
  gap-fills, bug hunts — is an item in day-based Leitner boxes: 1, 2, 4, 8, 16,
  32, 64 days, and a miss drops it to the front. Day-based, so the schedule runs
  while the tab is closed. New questions are metered in four at a time, so
  someone arriving mid-course meets "4 ready to review" instead of a wall.
- **The mistakes book.** Every miss is collected and drilled until it is
  cleared. A mistake you never see again is a mistake you keep.
- **Placement.** The welcome offers three doors. "I already know some of this"
  asks one question per grade and ticks off whatever you can prove, stopping at
  the first miss so nobody is skipped past a gap.

## Features

- Live preview on every keystroke; JS lessons enforce the house rule —
  *working it out is not showing it* — via the universal `.textContent =` check
  plus a `new Function` syntax gate with friendly error rewrites.
- **Give me a lead** reveals the answer in 4 word-snapped steps (scaffold, don't solve).
- **Ask a question**: offline keyword-matched answer bank (~230 entries).
- **Free play** sandbox (self-saving, uncheckable, unbreakable).
- Per-grade redo buttons, REMEMBER strip per language, reading level that
  "ages up" with the grades.
- Readable in both themes: every sampled piece of text meets WCAG AA contrast,
  and the test suite computes the real ratios from rendered styles so it cannot
  quietly regress. The coach's verdict is a live region, and the drill announces
  each question and verdict to a screen reader.

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
| 🧭 **The shape of it** (`SHAPE`) | subgoal labels (Margulieux, Catrambone & Guzdial) | The plan before you type: the solution's steps as plain-English goals with no syntax in them, plus a note naming the reusable pattern. Lessons that share a shape share phrasing on purpose. |
| 💬 **Say it in your own words** (`SAYIT`) | Explain-in-Plain-English (Lopez et al.; Murphy et al.) | After the tick, one sentence about what the code is *for*. Graded offline against synonym groups, generously. Never a gate, and a model answer appears either way. |
| 👣 **The footpath** | Khan talk-through ordering | Chips walk the learner through the page's stations in order, ending at the editor. |
| 👻 **The ghost coach** | worked-example fading | A guided lap where the next word types itself faintly, then a solo lap for the tick. |
| 🦆 **The duck** | rubber-duck debugging | Explain your own code aloud, one line at a time. |

Warm-ups (tiles, gap, bug, scrambled lines) disappear once a lesson is ticked;
the picture, the plan and the recall card stay. The review schedule lives in
`localStorage` under `srs`, answered say-it-backs under `saidok`, and the other
mechanics' XP under `teach2`.

Two things were deliberately **not** taken from the apps that popularised them:
hearts, energy and lives, which meter learning rather than teach it; and
leagues, leaderboards and streak pressure, which reward showing up over knowing
things. The daily streak stays because it celebrates without threatening.

After College graduation the course sends learners off to build a small real project of their own — the school is deliberately self-contained.

## For maintainers

The parser traps from the original build still apply: the inline script must
never contain the literal sequences for a closing body tag, an HTML comment
opener, or script open/close tags — they are built via string concatenation or
escaped (`safeJs`, `'<scr'+'ipt>'`). Test with the recipe in the original
HANDOFF: serve locally, click every lesson's "Show me" (all must pass) and
"Start over" (none may pass), and verify stripped-output solutions fail.

Per-lesson extras (`PRED`, `TRYIT`, `SHUF`, `TRACE`, `PICS`, `TILES`, `CLOZE`,
`BUGS`, `RECALL`, `TWIST`, `SHAPE`, `SAYIT`, plus `RN`, `MORE`, `OLDS`, `RW`)
are keyed by lesson index. Append new lessons at the end of their grade block
rather than inserting mid-array, or every downstream index shifts. `TWIST`
checks must be satisfiable while the lesson's own check still passes (ask for
additions, not swaps).

Post-graduation lessons carry `beyond: true`, live in their own `beyondDone`
set, and are excluded from `coreOf` / `coreTotal` so they never move the
graduation goalposts. Their `rn` / `rw` fields are carried on the lesson object
because `RN` and `RW` are declared after the lesson array is built.

There are two such grades now — Beyond and the Review Desk — and nothing keys
off either id. `beyondGrade(gid)` asks whether a grade is made entirely of
post-graduation lessons, and the sidebar, the hub's track rows, the hub's
next-thing, placement and the ghost coach all go through it. Adding a third is a
`GRADES.push` plus a builder that sets `beyond: true`, and nothing else.

**Writing a checker.** Where the point of a lesson is that something is
*removed*, the requirement must be a negative lookahead over the whole file
(`^(?![\s\S]*OLDTHING)`). A regex that only looks for the new thing will happily
pass a learner who added it and left the old thing sitting underneath — and in a
chain of `if`s, the old line is still the one that runs. Write the requirements
last, then test them against wrong answers, not just against your own solution.

**The test suites** live outside the repo but the recipe is worth keeping:
every non-project lesson must have its solution pass and its starting code fail;
every Beyond and Review Desk lesson additionally runs a list of
wrong-but-plausible submissions that must be rejected and alternative correct
solutions that must be accepted. That second list is what catches a checker that
is merely regex-shaped — it rejected `Math.max.apply(null, list)` and an arrow
`formatMoney` on the Review Desk's first run, both of them correct answers.

**Fact-check the prose against the running lab, not against your memory of
JavaScript.** Where a lesson claims what appears on screen or what error the
page stops with, load its start and solution into the real preview and read the
result off the iframe. The Review Desk's ninth lesson claimed the page dies at
`TAX_RATE is not defined`; it actually dies at `formatMoney is not defined`,
because a call's own name resolves before the arguments it is handed.

**Layout has a suite too,** because the two places it broke were the collapsed
sidebar and the phone. It sweeps every lesson at 1400 and 900 collapsed and at
390 and 360, checking every element against its panel's right edge, and it
asserts the typing column leaves no dead strip at four window heights.

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
