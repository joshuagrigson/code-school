# Code School — `code-lab.html`

> **Want to understand what you just created, past vibe-coding? Want full
> control over AI-assisted creations? #Code-School**

The complete Kindergarten-through-College coding class in one self-contained,
offline HTML file. Download it (or copy it to `C:\code-school\`), double-click,
and it runs in any browser with **zero network access and zero API usage**.

## What's inside — 192 lessons

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
| **Quest** | **8 levels where your code drives a hero across a board** |
| **The Sound Room** | **8 lessons where your code is the instrument** |
| **The Kata Table** | **7 puzzles marked on tests you were never shown** |
| **Python** | **13 lessons: a second language, from `print` to a working report** |
| **The Terminal** | **13 lessons: folders, files, pipes and git, typed by hand into a shell that lives in the page** |

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

All fifteen editor themes are available from the first minute of Kindergarten.
Making a learner earn a colour scheme gates comfort, not difficulty, and the
person most likely to need the light or high-contrast theme is the beginner who
has not earned anything yet.

Real progress lives in `localStorage` under `codeschool`, with the review
schedule under `srs`. A save code carries all of it to another device.

## The Arcade

Five grades that sit outside the school the way Beyond and the Review Desk do:
nothing here is needed to graduate, and none of it is a quiz. Each one is
lifted from a place that already worked out how to make programming feel like
something rather than like homework — and what was taken is the mechanic, not
the artwork.

**Quest** (from CodeCombat) is eight levels where your code drives a character
across a board. `hero.moveRight(4)`, `hero.attack()`, `hero.look("right")`.
Level one is five lines in a row; level eight takes the controls away and asks
you to write a `turn(hero)` function that something else calls sixty times,
which is the Screeps idea and a genuinely different way to think. In between:
an off-by-one that eats a corridor, an enemy that hits back if your maths is
wrong, and a switch that has to be stood on before a door three screens away
will open.

**The Sound Room** (from EarSketch) is eight lessons where the output is music.
`makeBeat(KICK, 1, 1, "0---0---0---0---")` — sixteen characters, sixteen slices
of a bar, `0` hits and `-` waits and `+` holds. There are no audio files in
this repository and there is no network, so every sound is *built*: a kick is a
sine wave falling from 150Hz to 45Hz in fifty-five thousandths of a second, a
hi-hat is filtered noise. The last lesson asks for eight bars with an
arrangement, which turns out to be a loop with an `if` on the bar number.

**The Kata Table** (from Codewars and CheckiO) is seven puzzles, ranked 8kyu to
5kyu, where you are shown two examples and marked on six or eight. The hidden
ones are deliberately the boring inputs — the empty string, the single item,
the all-negative list, the zero in the middle — because that is where real code
dies. Passing every example in the brief and failing the tests behind it is the
most useful hour in the whole place. The tests also catch a function that
quietly edits the list it was handed.

**Python** (from Sololearn) is thirteen short lessons and a real interpreter.
Not a transpiler and not a pretend one: a tokeniser that synthesises
INDENT/DEDENT from columns, a Pratt parser, and a tree-walker, all of it in the
same file. `7 / 2` is `3.5` and `7 // 2` is `3`; `print(1.0)` says `1.0` and
`print(1)` says `1`; `round(2.675, 2)` is `2.67`, because it rounds the decimal
expansion of the double rather than multiplying by a hundred first. It has
`UnboundLocalError`, because a lesson that lets you read a global you later
assign is a lesson teaching a falsehood.

**The Terminal** is the one track that needs no code first. Thirteen lessons,
each starting from a fresh copy of a small filesystem — a `project` folder with
an `app.js` and a `notes.txt`, a `scratch` folder with junk in it — and the
learner types commands, one per line: `pwd`, `ls`, `cd`, `mkdir`, `touch`,
`echo` with `>` and `>>`, `cp`/`mv`/`rm`, `grep`, pipes, `*` globs, and the
three lines of git that every project starts with. The shell is real in the way
the Python interpreter is real: a tokeniser that respects quotes, redirection,
`|`, `&&` and `#`, and a `git` that tracks a staging area and a commit history.
**The typing box is the terminal.** Not a script box, not a picture of a
prompt: on these lessons the editor is replaced by a terminal in the same
frame — type a line, press **Enter**, it runs and answers, `↑` recalls the
command before, a wrong line is answered rather than fatal. Everything run
collects in the editor's value underneath, so `Run`, `Show me`, `Start over`
and every checker still see an ordinary script; the terminal is the interface
and the script is the record.

**The panel below answers what a terminal never does: what did that do?** It
runs the same `shellRun` twice — once on nothing, for the machine as the lesson
handed it over, and once on the session — and draws the difference: files and
folders that appeared, changed or went, with the contents of the ones that
changed, then the whole tree as it now stands with a mark on the folder you are
standing in, and a git box once a repository exists. When a session has only
read, it says so in as many words: *everything you have run so far only looked*.
That distinction — looking versus doing — is most of what a beginner gets wrong
at a prompt, and a real terminal gives them nothing to see it with.

Getting here took three wrong shapes, each reported in one sentence by someone
using it: a static transcript that ran the whole box on `Run` ("shouldn't I have
to push enter"), an interactive preview with the editor still live above it ("I
never pressed enter" — the editor was running a line per keystroke), and a
read-only editor that swallowed the keys ("I can't even type in the top
section"). The lesson is the obvious one: if two things on screen can take
typing, exactly one of them is going to be wrong.

The coach does not grade the words typed; it grades the world left behind — is
the folder there, does the file say what it should, is the commit in, was the
repository started *inside* `site` rather than one level up. The preview is the
transcript, with the prompt showing which folder each command was typed in, so
`cd` can be seen doing something even though it prints nothing. Its errors are
in house style: `ls-l` is told about the space, `dir` and `cls` are told they
are the Windows words, `rm -r /` is refused, and a sentence (`Where am i?`) is
told it is a sentence and which program says that thing, because the first
goal line used to read like an invitation to type one, and the last lesson is a brief with
no walkthrough — scaffold a site and put it under version control — because
that is how the work arrives.

**The Adventurer** (from Codédex) is the character all of it belongs to: a name,
a face, and one of four classes — Builder, Sleuth, Architect, Bard — which are
dispositions towards programming rather than costumes. The class picks your
badge track and which arcade door opens first. The figure walking the Quest
board is the face you chose. Twelve badges, each one earned by something that
ran.

The two ideas taken from **Brilliant** and **CodinGame** are already everywhere
in the school rather than parked in a grade: one concept then immediately a
question you cannot skip (the recall cards and the predict-the-output gates),
and a visible replay of what your code did rather than a verdict about it —
which is why Quest animates the run command by command, and why the Sound Room
draws the score it is about to play. **CodingForKids**' block-to-text bridge is
the strip of coloured command blocks under the Quest board: your program, as
blocks, highlighting the one currently running.

### One engine, two jobs

Quest, the Sound Room and the Kata Table each have exactly one simulator, and
it is a pure function. The coach grades its result; the preview animates the
same result. There is no second copy for the two to disagree about, which is
the failure that makes a game like this feel rigged — a board showing the hero
on the flag while the marker says you missed it. `questRun` is written
self-contained on purpose: the preview gets it by calling `.toString()` on it
and injecting it into the iframe.

Python, the katas and the Terminal do not need a script in the preview at all —
the interpreter, the test runner and the shell live in the page, and the preview
is handed the finished console, table or transcript as static HTML. `shellRun`
records the working directory on every transcript line as it was *before* the
command ran, which is what the prompt needs and what a post-hoc replay gets
wrong. It also keeps running after a line fails, the way a real prompt does —
only a broken lesson `pre` stops the session — while `error` stays the *first*
complaint, so the coach's verdict does not move.

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

## The look

Two themes, both designed rather than inverted from each other, and both built
to be taken seriously by the adult typing alongside the nine-year-old.

- **Warm paper in light, warm graphite in dark.** Not blue-grey; not pure black.
  Surfaces separate by tone (`--panel` over `--bg` over `--panel2`), so the
  structure survives even where a border would be invisible.
- **One accent, spent sparingly.** Deep green for what you act on, deep navy for
  what you are being told. Everything else is neutral.
- **Hairlines and three depths.** Every card border is 1px; separation comes
  from `--sh1` / `--sh2` / `--sh3` and nothing invents a fourth. The coloured
  bar on a teaching card is a 3px marker, not a stripe.
- **A serif for the things that matter** — lesson titles, the hub's greeting,
  the certificate. It reads as a storybook to a child and as an editorial to
  their parent. No webfonts: this file makes zero network calls, so the stacks
  (`--serif`, `--sans`, `--mono`) have to be good on their own.
- **Tabular numerals** on every counter, so progress never makes the line jump.

### Fifteen looks for the editor, none of them earned

Classic Dark, Midnight, Paper, Synthwave and Phosphor, plus Solarized Dark and
Light, Dracula, Nord, Gruvbox, Monokai, One Dark, Cobalt, Amber CRT and
Commodore. All available from the first minute — a colour scheme is comfort, not
a reward, and the learner most likely to need the light or high-contrast one is
the beginner who has not earned anything yet.

Where an authentic palette put a token below AA on its own background — Monokai's
comment grey, Dracula's `#6272a4`, One Dark's `#5c6370` — the hue is kept and
only the lightness is raised, solved numerically against that theme's background
rather than by eye. The faint "ghost" text the coach types ahead is placed on the
line between the theme's foreground and its background at whatever point clears
5:1, so it still reads as faint without becoming unreadable. These are read by
nine-year-olds on laptop screens in daylight.

### Contrast is not a matter of taste here

The suite computes real WCAG ratios from rendered styles, so a palette change
that fails AA fails the build. There are two levels: `suite.js` samples about
nineteen representative points, and `contrast_sweep.js` walks **every element
with a direct text child** across fourteen screens in both themes, composites
every translucent layer down to the first opaque ancestor, folds each element's
own opacity into its text colour, and additionally checks that both token blocks
declare the same names and that all fifteen editor themes read.

The sampled version passed while ten real failures were live, including the
ghost coach at 1.59:1 and the Paper theme rendering HTML attributes at 1.40:1.
The sweep is the one that finds them.

## On a phone

The phone is a first-class layout, not a narrowed desktop.

- Two deliberate header rows — who you are and how far you have got, then the
  actions sharing the width evenly — instead of a ragged wrap.
- The tab bar pads past the home indicator (`env(safe-area-inset-bottom)`),
  frosts what scrolls under it, and marks the active tab with a rule rather than
  a colour change alone. `viewport-fit=cover` and a `theme-color` that follows
  the light/dark toggle, so the browser's own chrome matches the page.
- The action row sticks to the bottom of the editor column: **Run** is always
  under a thumb, on every lesson, without scrolling.
- Nothing tappable is under 34px. The lesson crumb drops its repeated grade
  subtitle to earn its one line. Code samples wrap instead of hiding behind a
  sideways scroll.

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

**The arcade's two new languages.** `lang:'arc'` (Quest, the Sound Room, the
Kata Table, the Terminal) and `lang:'py'` bypass the JavaScript branch of
`runCheck` entirely, because that branch insists on a `screen.textContent =`
line, which is right for a page and wrong for a level, a song, a kata and a
`print()`. They are graded by running them: the engine's own result is a better
error than anything a regex could say about it. `normRes` skips the DOMParser
for both, and `stylePass` is replaced by `pyStyle` for Python, because the
brace-counting indent check calls every correctly indented Python program badly
indented. The `arc` lessons also get a JavaScript parse before the engine sees
them, so a missing bracket is explained in the coach's English — except
`kind:'shell'`, which is not JavaScript and skips it: `echo "<h1>Hi</h1>" >
page.html` is a perfectly good line of shell and a syntax error in anything
else.

**A Terminal lesson is a filesystem plus a question about the filesystem.**
`SH(...)` takes a `spec` — `{fs, cwd?, pre?}` — where `fs` comes from
`shfs({'project/app.js': '...', 'scratch': null})`, a flat path map because a
nested tree literal is unreadable for anything real, and `pre` is a list of
commands run silently before the learner's so a git lesson can start in a
repository that already has a commit. The tests are a function of the finished
state: `st.isDir('site/css')`, `st.read('notes.txt')`, `st.git.commits.length`,
`st.git.root === '/home/you/site'`. Errors are numbered from the learner's first
line, not from the first `pre` line, and `st.ran` never includes the `pre`
commands — a lesson must not pass because the setup typed `git init` for you.

**The engines are written as self-contained functions on purpose.** `questRun`
and `soundRun` are serialised with `.toString()` into the preview iframe, so
they must not close over anything outside themselves. `ARC_CSS` and its
siblings are JSON-encoded JS strings inside the script, so a rule added to one
needs `\n` escapes, not real newlines — a comment with a real line break in it
breaks the file, and only a parse check catches it.

**A runaway loop is guarded in the loop's condition, not its body**, because
`while (true);` has no body to put a counter in. Both the arcade engines rewrite
`while (` to `while(__tick(),` and the middle clause of a three-part `for`, so a
loop with no braces is still stopped.

**Every lesson's own answer is tested against its own checker,** and its
starting code against the same. Three of the eight Quest levels failed that on
their first run — the boards were unbeatable by the solutions printed
underneath them, including one where a memoryless `turn()` rule oscillated
between two squares forever. Trace a level in Node before writing prose about
it.

**The prose makes falsifiable promises, so they get tested.** The Python track
makes forty claims about what the interpreter does — that `input()` always
hands back text, that `[::-1]` reverses, that `round(2.675, 2)` is `2.67` — and
each one is a case in `py_claims.js`, run against the interpreter in the page.
The kata lessons promise that particular naive answers fail particular hidden
tests; those are `kata_claims.js`. One claim was wrong on the first run: the
unguarded `titleCase` was said to hand back `undefined`, and it actually stops
with a TypeError. The prose changed, not the code.

**Use a real click in a Playwright harness, not `element.click()` inside
`page.evaluate`.** A synthetic click in the same tick as a layout change leaves
the preview iframe unlaid-out, so every lesson — including a Kindergarten one
that predates all of this — reports an inner body height of zero and screenshots
blank. That is the harness, not the page. It is the second time a measurement
artifact in this file has nearly been "fixed" as a defect; the first was
sampling during a CSS transition.

**Contrast in the preview needs its own sweep.** The main sweep skips `#out`
deliberately, because that frame is normally the learner's own page. In the
arcade it is ours — verdict banners, a HUD, a test table, a console — so
`arc_contrast.js` sweeps inside the frame with the same maths, on fourteen screens
in both themes. It found the celebration banner at 2.79:1 in dark mode, which
had been there all along and which the arcade now fires forty-four more times.
It also reports emoji, whose CSS colour is not what you see; the sweep skips
text with no alphanumerics in it.

**Publishing.** `.github/workflows/pages.yml` builds and deploys the site on
every push to `main` (and on demand, via *Run workflow*). It runs the same
github-pages Jekyll build over the repository root that GitHub's own generated
job ran, so `course/*.md` keeps rendering into the `course/*.html` pages that
are linked — a plain static upload would serve those as raw markdown. The
workflow exists because GitHub's internal push hook for Pages went quiet on
this repository: pushes landed and no build was ever queued, and the only way
to publish was to re-save the source in Settings. A deploy you can see, re-run
and read the logs of is worth more than one that happens invisibly until it
doesn't. Pages **Source** must be set to *GitHub Actions* for it to deploy.

**The words you type are chips.** Inline `code` in a lesson has its own
ground, edge and ink rather than being prose in a different font, and inside a
chip the command itself is stronger again — in `echo milk > shopping.txt` one
word is the machine's and three are yours, and nothing on the page said which
until `markCode` marked them. The word lists are per track (`KEYWORDS`), the
marking runs over the rendered lesson and goal rather than the source, so no
lesson text had to be rewritten, and `chip_test.js` walks every lesson in the
school to check that a chip is visibly a chip in both themes, clears AA on its
own ground, and that the commands it knows about are marked.

**A printed code block makes a promise, so it states it.** Every `pre.czcode`
in a lesson is captioned by running that lesson's own checker on it: *this is
the answer*, *these lines belong in your answer but are not all of it*, or *an
example of the idea, not the answer*. It came from someone typing the block on
the last Sound Room brief exactly as shown and being marked wrong — correctly,
because it demonstrates the trick with two tracks where the brief wants four.
Deriving the caption from the checker rather than from a hand-written note
means it is right on all 27 blocks and stays right; the first version guessed
from text overlap and told eight lessons' worth of learners that a block
"belongs in your answer" when typing it alone still failed.

**The rhythm string explains itself.** Every Sound Room lesson draws its own
pattern as sixteen labelled slices with the beat count underneath (1 e & a 2 e
& a…), the four beats marked, and `0` / `-` / `+` given meanings in words,
plus the four arguments of `makeBeat` colour-matched to an explanation of each.
Reported as "the dashes arent clear what they mean", which the prose had in
fact explained in a sentence — a sentence is not the same as being able to see
which character is which slice.

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
