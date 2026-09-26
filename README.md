# Code School — `code-lab.html`

> **Want to understand what you just created, past vibe-coding? Want full
> control over AI-assisted creations? #Code-School**

The complete Kindergarten-through-College coding class in one self-contained,
offline HTML file. Download it (or copy it to `C:\code-school\`), double-click,
and it runs in any browser with **zero network access and zero API usage**.

## What's inside — 234 lessons, and a path

Graduation is the 155 required lessons — every lesson, every practice rep, every
challenge, the arcade prep lessons inside the grades, and the boss at the end of
each grade. Portfolio pieces, Beyond and the Review Desk sit outside that count.

| Track | Territory |
|---|---|
| K–1 | HTML: tags, attributes, lists, buttons, links, boxes |
| 2–3 | CSS: colors, spacing, borders, classes and ids |
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
| **Quest** | **16 levels where your code drives a hero across a board that fights back** |
| **The Deep** | **650 generated Quest floors, each one proved winnable before you see it** |
| **Grade bosses** | **14 Quest boards, one at the end of every grade from Kindergarten to College, each asking for that grade's idea somewhere it was never taught — and each one required to finish the grade** |
| **The Sound Room** | **8 lessons where your code is the instrument** |
| **The Puzzle Vault** | **7 vaults shut by tests you were never shown: a tumbler per test, keys cut by school lessons, a relic wall and a jigsaw the whole school fills in** |
| **Python** | **13 lessons: a second language, from `print` to a working report** |
| **The Terminal** | **13 lessons: folders, files, pipes and git, typed by hand into a shell that lives in the page** |
| **Learn Python** | **The Duolingo mechanic pointed at Python: a path of 21 units, eight quick cards a session, five kinds of card, every one built from real code by the engine** |
| **Arcade prep** | **28 small Terminal, Python, Sound Room, Puzzle Vault and Quest lessons inside the grades themselves — K through College — so each arcade room is somewhere you have already been** |

Reviews double as test-out exams (⚡): pass one first and it ticks the lessons
it examined — not the challenge, the prep or the boss, which the walk then takes
you to. Challenges are hint-free and pay +25 XP on top, but they are lessons of
the grade like any other. Reps (🏋) count too, because the practice most likely
to make something stick was the practice easiest to skip. Beyond and the Review
Desk sit outside the graduation count on purpose — they are what you do after
finishing, not a moved goalpost.

**Nothing at the end of a grade is optional, and a pass moves you on.** Within
a grade the walk is: the lessons, the reps, the challenge, the arcade prep, the
boss — all of them in the sidebar from the start, all of them in the grade's
x/y. When you pass a lesson the coach's verdict stays on screen for six
seconds with the Next button counting down, and then the next lesson not yet
done loads by itself. Clicking goes now. Typing again holds it — a twist or a
second attempt is work, not a way out — and the countdown starts again on the
next pass. A failing run never moves you. The Deep keeps its own *Descend*.

## The boss at the end of every grade

Fourteen Quest boards, one per grade, each one required to finish its grade. Each takes the
single idea that grade spent its lessons on and asks for it somewhere with
nothing in common with where it was learned: a page becomes a dungeon, and the
idea either travelled or it did not. Grade 1 taught that elements have names,
so its boss makes you hit two ogres by name. Grade 6 taught lists, so its boss
hands you a list of step counts to walk. Grade 9 taught loops, so its boss
spaces three enemies evenly and blocks the nine-line answer with a move budget.
Grade 12 taught debugging, so its boss starts with a program that is already
wrong and asks you to read the note under the board.

None of them can be passed by walking at the flag — that is a test, not a claim
— and every one ships with the answer that beats it, checked by the same engine
the learner plays on. An idea you can only use in the room you met it in is a
memory.

## The arcade, inside the grades

The five arcade rooms used to start from nothing at the end of the school. Now
each grade carries one or two short lessons in those languages, pitched at the
grade's own idea, as core lessons that count toward the grade and toward
graduation — that is what "part of the main lessons" has to mean. Five ladders:

- **Terminal** K → 1 → 3 → 10 → 12 → College: `ls` → `cat` by name → `mv` as a
  name you can change → build in stages, reading the panel after each → `grep
  -r TODO` → a commit whose message is a sentence.
- **Python** 4 → 12 → College: `print` → `2 + 3` vs `"2" + "3"` → a list and
  `len` → `def` → `if`/`else` → `for` → a dict → a program that starts with a
  real `TypeError` → a docstring.
- **Sound Room** K → 2 → 5 → 9: copy one line and hear it → color in slices 1
  and 9 → the tempo is a number → a loop lays two bars.
- **Puzzle Vault** 7 → 8 → 9 → 11 → 12 → College: `double` → `sign` with the
  case the examples never show → `sumAll` → `nameOf` → fix `lastOf`, which
  starts off by one → `isEven`, returning the expression.
- **Quest** 1 → 4 → 8: walk to the flag by name → `say(look())` → an `if` that
  steps round a wall.

Each one ends with a note saying which room it is a first taste of. Every Quest
board and puzzle was proved on the real engine before it was written in — the
answer wins and the starting code does not — and the browser test does the
same for all 28 through the page's own grader.

Mechanically: `PREP(gid, tag, builder, args)` calls the room's own builder and
then re-homes the lesson — `g` becomes the grade, `beyond` becomes false — so
the engine, the coach and the chips are exactly the room's. They are appended
to `L` after everything else, because saved progress is a list of lesson
indexes and inserting in the middle would point every save at a different
lesson than yesterday; `ORDER` ranks each grade's entries (lessons 0, reps 1,
challenge 2, prep 3, boss 4, stable within a rank) whatever their index, and
`walkOf(gid)` is what the sidebar and the crumb read, so the three agree.
Old saves keep their credit: `chalDone` and the boss entries in `beyond` are
folded into `done` on load. The ghost coach is off for Terminal
lessons (the editor is behind the prompt there, so a ghost typing into it is a
coach nobody can see), the crumb no longer counts the boss in "lesson n of m",
and the level titles were recomputed so "Loop Rider" still lands on the loops
lesson it always did rather than a grade later.

`prep_test.js`: 35 checks.

## Learn Python: the path

The mechanic a hundred million people use every day, pointed at Python. A path
of 21 small units — print, numbers, words, boxes, `if`, `elif`, `while`, `for`,
lists, slices, strings, dicts, functions, `return`, defaults, `try`, small
programs — each a five-minute session of eight cards. Five kinds, rotated so no
two in a row are the same: **read it** (what does this print — pick one),
**fill the gap** (type the missing piece), **type it** (type the last line
yourself), **order the lines** (tap them into place), **find the bug** (which
line is wrong). Instant verdict on every card with a sentence saying why.
Three hearts a session; a wrong card is dealt again at the end, and keeps
coming back until it is right. A crown on the unit when you clear it, the
next unit unlocks, XP and the streak tick. Out of hearts ends the session and
loses nothing.

None of the cards were written by hand. `LP_UNITS` is 105 short snippets with
a sentence each; everything else is built from them by running the real
Python engine. A read card's right answer is what the engine printed; its
wrong answers are what the engine printed for the snippet with **one thing
changed** (`LP_MUT`: a number off by one, `<` for `<=`, `and` for `or`,
`.upper()` for `.lower()`, `range(n)` for `range(n+1)`, two lines swapped…),
kept only if the engine says the output differs. A find-the-bug card is one
of those mutants, restricted to the ones that changed a single line. A
fill-the-gap answer is right if it is the original token *or* if the engine
says the program it makes prints the same thing — and a blank is only offered
where a nonsense token would change the output, because a token inside a
branch that never runs would accept anything. A typed line and an ordered
set of lines are checked the same way: run it, compare. `input()` snippets are
kept off the read cards, since the console echoes what was typed.

`lp_test.js` builds 252 sessions (every unit, twelve seeds) and holds every
card to it: exactly one right option, all options distinct and real, the
snippet's own answer accepted, nonsense rejected, a missing line rejected,
the bug's fix restoring the expected output. Then it plays a session through
the buttons a person presses, misses on purpose, and checks the hearts, the
re-deal, the crown, the unlock, the XP and the streak.

## The Sound Room shows its working

**The studio.** The Sound Room's preview is a drawn studio console. Your hero
performs on a little stage (string lights, spotlight, speakers) in its own
class style — the skald strums with notes flying, the knight and the barbarian
stomp and shake the stage on the downbeat, the others step in time with their
own footfall, the mage's runes pulse — and takes a bow when the beat passes. A screen shows a live spectrum and
waveform while it plays (tapped after the mix, so the sound is unchanged), with
tempo, bar and beat readouts. Every track has a channel strip with a drawn
instrument icon, its own color and a level meter; the grid is glowing pads,
held notes as solid bars, and a playhead that sweeps in time with the audio.
Effects show as drawn knobs. Nothing plays until you press Play.

The room's whole language is a sixteen-character string, and for a while it
taught that language by assertion: *beats 2 and 4 — slices 5 and 13*, with
nothing on screen connecting the first half of that sentence to the second.
Someone who typed `makeBeat(SNARE,` and stopped had been told *where* without
ever being shown *how*, and the only way to check a string was to press Run and
be told no.

Three things fix that, and all three are on every lesson in the room:

- **The numbers are derived, not stated.** The panel under each lesson lays
  out the sixteen slices *with their numbers on them*, then shows why a beat is
  four of them, which slice each beat starts on (1, 5, 9, 13), why an eighth is
  every other slice, and a method for typing sixteen characters without losing
  count (four groups of four). Lesson 2 works the method on a *different*
  target — a hit on beat 3 — so the snare string is derived by the learner, not
  handed to them.
- **Every string you type is read back to you.** Press Run and the board
  echoes each `makeBeat` with the slice numbers under its characters and says
  in English where the hits landed: *2 hits, on slices 4 and 13 — the a after
  beat 1 and beat 4.* A hit one slice early is named as what it is.
  Fifteen characters is counted and said; seventeen is told where it spills.
  `fitMedia` is read the same way — *measures 1, 2, 3 and 4, stops before 5* —
  which is the half-open range lesson 6 is about, shown rather than described.
  It reads the calls the engine actually made, so a loop's bars are read the
  same as a typed one, once.
- **The board is numbered** — slice numbers under the rows, beats marked — and
  it stops padding a second, empty measure nobody wrote.

`sound_teach.js` holds the room to all of it, including that lesson 2's teach
text never contains the snare string and that a fifteen-character rhythm is
caught before Run.

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
Making a learner earn a color scheme gates comfort, not difficulty, and the
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

**Quest** (from CodeCombat) is sixteen levels where your code drives a
character across a board. `hero.moveRight(4)`, `hero.attack()`, `hero.look("right")`.
Level one is five lines in a row; level eleven takes the controls away and asks
you to write a `turn(hero)` function that something else calls sixty times,
which is the Screeps idea and a genuinely different way to think.

That level used to arrive straight after the first `look`, and its answer needed
`!==`, `&&`, `||`, `else if` and `look("down")`, none of which the track had
taught. Three levels now come first, each adding one of those words on a board
where the previous level's rule fails, so the new word is needed rather than
decorative. *Not a wall* starts from the rule most people write first
(`=== "clear"`) and shows it refusing to step onto a gem. *The wall and the
edge* puts a wall and the map's edge on one board, so a rule has to rule out
both, and shows `&&` and `||` as two ways to say it. *Plan B, plan C* asks the
same question pointed down and adds an `else if` chain.

Each of the three is laid out the same way: run it and watch; a drawing of
that board with the squares where the hero goes wrong numbered; a table of
what `look` answers there and what each question says yes or no to; the one
line to change, before and after, with the new part highlighted; then a
fill-the-gap on the new word, where a wrong pick says why it is wrong.

**Every lesson in the school is taught that way now**, not only Quest: all 209
other lessons (K through College, the Hustle, the Portfolio, the Machine Room,
Beyond, the Review Desk, the Sound Room, the Puzzle Vault, Python and the
Terminal) and all 21 Learn Python units.

- **What you are making**, generated from the lesson's own answer: the page it
  builds (drawn into a shadow root, so the lesson's styles stay inside and
  nothing in it runs or fetches; images become a labelled box), what it prints
  (Python, worked out by the in-page interpreter), the tests it must pass
  (the Puzzle Vault) or the folders it starts in (Terminal). JavaScript answers are run
  once and what they show is kept; `allcover_test.js` re-runs them to prove the
  pictures still match. The Deep draws each floor's board from the route its
  generator proved, without handing that route to Show me.
- **Do it in three steps** with the key line marked, a table where one helps,
  a fill-the-gap and a reminder line of its own. These were written per lesson
  and then held to the lesson by a validator: every marked key line appears in
  that lesson's answer (for a project, in the code its brief gives), and every
  gap, filled in, is a line of the answer. The same check runs in
  `allcover_test.js`, so changing a solution later cannot leave a guide
  teaching the old one.
- **Learn Python** opens each unit with *How this unit works*: the three steps
  and the unit's five examples with what each one prints, worked out by
  running it, above the first card. Open the first time, folded once crowned.
- JavaScript that does not parse yet is no longer run in the preview; it says
  calmly that nothing has run, and the coach under the editor says why.

**Every Quest board is taught that way now**: the sixteen levels in the track,
the fourteen grade bosses and the three prep boards inside the grades. Each
lesson shows a drawing of its board with the route the answer takes and every
event on the way numbered (a gem, a switch, a fight, a lost heart, a wait).
The drawing is generated in the page from a replay of the answer on the real
board, so it cannot drift from the level. Under the lesson sit three steps
with the key line highlighted, a table where one helps (fight arithmetic, loop
laps, spike timing), a fill-the-gap on that lesson's idea, and a reminder
line of its own. `qcover_test.js` fails the build if any Quest lesson is
missing one of those. *The witch down the hall* now gives you one heart, so
the board itself insists on stepping out of her row first, which is what the
lesson teaches.

Those three are judged by their boards, not by which operator you typed: any
rule that gets the hero there passes, and a rule that leaves out the new idea
fails visibly, with the hero stuck on the board. `ladder_test.js` holds them to
that for nine different ways of writing the rule. When a Quest level is cleared but
something it teaches is missing (a hard-coded route instead of a loop, say),
the checklist says the hero made it and that this is the part being taught. The last of those rules, moved inside `turn`, is the answer to
level eleven, so that level teaches one idea: who runs the rule. In between:
an off-by-one that eats a corridor, an enemy that hits back if your maths is
wrong, and a switch that has to be stood on before a door three screens away
will open.

The last five levels are a board that does not wait for you. **The world takes
a turn after every one of yours** — every move, every swing, every `say` — so a
wasted line is a square of ground given away. A *chaser* walks toward you, a
*patrol* walks its beat, a *ghost* ignores walls, and a *caster* never moves but
owns her whole row and column until you step out of it. Spikes come up on a
count, which makes a deliberate wasted turn the answer rather than a mistake,
and a pit is not a heart but the end of the run. Every one of them turns a route
into a strategy: `look`, decide, act, repeat, against a board you cannot
predict — which is the loop every robot and autopilot ever written runs.

The whole kit is synthesised through the Sound Room's own `soundKit()` bus, so
the replay has a voice: a sword is filtered noise with a crack on the front, a
defeated ogre is a sawtooth falling through a filter, and clearing the level
gets a chord. There is a sound toggle on the board and the page remembers it.

**The Sound Room** (from EarSketch) is eight lessons where the output is music.
`makeBeat(KICK, 1, 1, "0---0---0---0---")` — sixteen characters, sixteen slices
of a bar, `0` hits and `-` waits and `+` holds. There are no audio files in
this repository and there is no network, so every sound is *built*: a kick is a
sine wave falling from 150Hz to 45Hz in fifty-five thousandths of a second, a
hi-hat is filtered noise. The last lesson asks for eight bars with an
arrangement, which turns out to be a loop with an `if` on the bar number.

**The Puzzle Vault** (after Codewars and CheckiO) is seven puzzles, from a brass
lock to a master lock, where you are shown two examples and marked on six or eight. The hidden
ones are deliberately the boring inputs — the empty string, the single item,
the all-negative list, the zero in the middle — because that is where real code
dies. Passing every example in the brief and failing the tests behind it is the
most useful hour in the whole place. The tests also catch a function that
quietly edits the list it was handed.

Each puzzle is drawn as a vault door with one tumbler per test. Run it and your
hero works the tumblers in turn with its class move; a passing test clicks home,
a failing one jams and its row in the table says why, and a door with every
tumbler turned swings open on that vault's relic. The vault hall holds the seven
doors, a key ring (Functions, Loops, Strings, Lists, Conditions and Objects,
each cut by the school lesson that teaches it — a missing key never locks a door,
it links to that lesson), the relic wall, and a picture that gains one jigsaw
piece for every core lesson finished anywhere in the school.

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

**The Deep** is the same hero on six hundred and fifty boards nobody wrote.
A floor is not stored: it is built from its own number, so floor 137 is floor
137 on every machine, forever, and the whole dungeon costs one entry in the
lesson list rather than 650. The interesting part is the promise. Generated
levels are notorious for shipping rooms with no doors, so before a floor is
handed over the generator lays a route through it, writes that route as a
program, and runs it through **the same `questRun` the learner plays on** — if
the real engine does not win, the floor is thrown away and a different one is
built. A floor nobody can finish cannot exist, and the proof is not a model of
the game but the game. `par` is what that plain route cost: walk, swing at
whatever is in the way, wait when the spikes are up. Beating par means you
found something better than the machine did.

**The Adventurer** (from Codédex) is the character all of it belongs to: a name,
a drawn hero, a species and one of eight warrior classes, each a disposition
towards programming as well as a way to fight. The class picks which arcade door
opens first. The figure walking the Quest board is the hero you made, and it
grows as you finish grades. Fourteen badges, each one earned by something that
ran.

| Class | Fights with | The programmer underneath | First door |
|-------|-------------|---------------------------|------------|
| Knight | sword and shield | finishes; ships it end to end | Quest |
| Ranger | longbow, later a hawk | reads the whole error message | Puzzle Vault |
| Mage | staff, later a codex of runes | wants the shape to be right | Python |
| Skald | drum, later a war-horn | wants it to feel and sound right | Sound Room |
| Barbarian | hatchets, later a great cleaver | tries it and sees | Quest |
| Guard | spear and shell shield | guards the edge cases | Puzzle Vault |
| Monk | fists or a staff | practises a little every day | Learn Python |
| Artificer | wrench, later an arc-cannon and a drone | builds the tools | Terminal |

The first four are the old Builder, Sleuth, Architect and Bard grown up: a save
with one of those classes loads (or imports) as the knight, ranger, mage or
skald with the same look.

**Species.** Human, elf, dwarf, orc, saurian or foxfolk, each with its own head
and face and its own lists: skin tones (scales for a saurian, fur for a fox) and
hair (beards for a dwarf, crests and frills for a saurian, ears for a fox). A
save without a species is the human it always was.

**Tiers.** The hero has five tiers, read off the grades you have finished (every
core lesson of the grade done), never stored and never gating anything: Recruit
(everyone starts here), Squire (Grades 1–3 finished), Veteran (4–6), Champion
(7–9) and Legend (10–12; College is not needed). Each class has a form name per
tier — the knight goes from Village Recruit to the Gilded Paladin, the artificer
from Tinker Recruit to the Arcwright Colossus — and its gear, its effects and
(for the ranger and artificer, from Champion) a companion grow with it. A learner
already deep in the school arrives geared up; finishing the grade that raises
the tier announces the new form once, in the badge toast queue.

**Code-themed gear.** The runes of this world are code. Every grade boss drops
one piece of gear per class (fourteen, Kindergarten to College), and each carries
the sign of what that grade taught: the `;` of a first line, a `</>` tag, a `#`
color, an `x=` name tag, the `=>` of an event, `[ ]` lists, `( )` functions,
`?:` choices, the loop arrow, and at the top `{ }` runes that glow. The signs
are drawn on the hero (never as text), and the character sheet lists the gear
you have earned by beating each boss, with the rest as quiet silhouettes.

### The hero, the monsters and the map

The hero used to be an emoji, so it looked like whatever font the machine had.
It is drawn now, in one art direction shared with everything it meets:

- **A character creator.** Your hero stands on a lit stage while you pick a
  name, one of eight classes (each card shows your hero as that class's
  Recruit), a species and a look: skin (or scales, or fur), hair (or beard,
  crest, ears), 10 hair colors, 6 eye styles, eye color, 10 extras and an
  outfit tint per class. Randomise rolls the species too, and only ever picks a
  look that works. Under the stage a tier bar names the tier and form you have
  reached, and **See your final form** shows your class as a Legend.
- **Every class moves its own way.** The knight chops and shakes the board, the
  barbarian cleaves and shakes it harder, the ranger looses an arrow, the mage
  casts a bolt, the guard thrusts, the monk throws a flurry, the skald drums
  (and from Champion blasts the war-horn) and the artificer swings a wrench (and
  from Champion fires the arc-cannon). The mage, skald, guard and monk have an
  idle effect too, and the barbarian and artificer gain one as Veterans. The creator's stage, the Quest
  board, the Sound Room and the vault doors play the same moves at your tier.
- **Ten monsters, each with its own moves.** Grubb, Mott, the Ogre, the Imp,
  the Warg, the Demon, Vex, the Wisp, Mordra and the Drake. The imp hovers and
  swoops, the warg wags and lunges, the casters charge and fire beams down
  their row, the drake sleeps until something wakes it and then breathes fire.
- **A board for every zone.** The four Quest zones (the Cellar Steps, the
  Guardroom, the Thinking Halls, the Lower Vault) and the Deep each have their
  own tileset: walls with depth, animated fire, pits, spikes that visibly rise
  and fall, a portal exit, a light that follows the hero, hearts and gems and a
  moves meter as the HUD.
- **The Deep is Quest's floor.** It is not a door of its own: the Quest map's road
  ends at its stairway, which shows your floor, and the Quest card in the arcade
  carries a small picture of it and how far down you are.
- **A map to choose levels from.** Entering Quest opens an illustrated map: the
  road runs through the four zones, every level is a medallion (gold when
  cleared, glowing where you left off, with your hero standing on it), and each
  level's monsters wait beside it. Nothing is locked. A Map button on every
  Quest lesson goes back to it.
- **Fights read clearly.** A swing holds until its blow lands and a kill holds
  until the monster falls, so the hero never walks on before the hit. A loss
  ends on the hero knocked down with a DOWN label; on a wide, short preview the
  HUD moves beside the board so the board can be bigger.
- **A character sheet** with your hero in a class frame, your tier and form
  ("Veteran · Sparkwrench Veteran"), your stats, the road of five tiers with
  your hero drawn at each and the grades that earn the next one, the gear you
  have earned from the grade bosses, and the badges as drawn medals.

Old saves keep working: a save from before the drawn hero carries only an emoji
face, so a hero is grown from that face and the name — the same save always
grows the same hero — and a save from before the warrior classes keeps its look
under the class it grew into. Every sprite and animation is inline SVG and CSS inside
the one file, and `prefers-reduced-motion` stills all of it.

The two ideas taken from **Brilliant** and **CodinGame** are already everywhere
in the school rather than parked in a grade: one concept then immediately a
question you cannot skip (the recall cards and the predict-the-output gates),
and a visible replay of what your code did rather than a verdict about it —
which is why Quest animates the run command by command, and why the Sound Room
draws the score it is about to play. **CodingForKids**' block-to-text bridge is
the strip of colored command blocks under the Quest board: your program, as
blocks, highlighting the one currently running.

### One engine, two jobs

Quest, the Sound Room and the Puzzle Vault each have exactly one simulator, and
it is a pure function. The coach grades its result; the preview animates the
same result. There is no second copy for the two to disagree about, which is
the failure that makes a game like this feel rigged — a board showing the hero
on the flag while the marker says you missed it. `questRun` is written
self-contained on purpose: the preview gets it by calling `.toString()` on it
and injecting it into the iframe.

Python and the Terminal do not need a script in the preview at all — the
interpreter and the shell live in the page, and the preview is handed the
finished console or transcript as static HTML. The Puzzle Vault's test runner
lives in the page too; its preview gets the finished table plus the word for
each test, `set` or `jam`, and only plays the door. `shellRun`
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
- **The arcade, up front.** The arcade is the one place with games in it, so it
  is not a tile among tiles. It has its own button in the header, next to Hub,
  lit whenever you are in the arcade or inside one of its rooms. On the hub it
  is a band just under the next step: all seven rooms as picture doors with
  your progress on each, one tap from the room itself.
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
  from `--sh1` / `--sh2` / `--sh3` and nothing invents a fourth. The colored
  bar on a teaching card is a 3px marker, not a stripe.
- **A serif for the things that matter** — lesson titles, the hub's greeting,
  the certificate. It reads as a storybook to a child and as an editorial to
  their parent.
- **Three typefaces, carried inside the file.** Inter for the interface,
  Fraunces for headings and JetBrains Mono for code, each a Latin-subset
  variable font embedded as base64 (about 170 KB together). The file still
  makes zero network calls, so the lab looks the same on a school laptop with
  no internet as it does on a designer's monitor. Code ligatures are switched
  off on purpose: a learner typing `!=` must see `!=`, not a `≠` glyph they
  cannot find on the keyboard.
- **Tabular numerals** on every counter, so progress never makes the line jump.

### Drawn, not typed

Emoji look different on every device and cheap on most of them, so every
picture the interface relies on is drawn as SVG inside the file.

- **One icon set** of stroked 24px glyphs in `currentColor`, used in the header,
  toolbar, tab bar and footer. Labelled header buttons drop their icon on narrow
  phones so the words still fit.
- **The sidebar marks each kind of lesson** (review, reps, challenge, terminal,
  Python, sound, puzzle, boss) with its own colored glyph. The original title
  text stays in the markup, visually hidden, so search, screen readers and the
  tests read exactly what they read before.
- **Arcade doors, the welcome card and the Learn Python path** have their own
  illustrations: a door picture per room, a scene for the first screen, and
  drawn crowns, locks, hearts and streak flames on the path.
- **Quest has a tileset.** Floors, walls, pits, spikes, fire and the exit are
  48x48 drawings lit from the top, so the board stays sharp at every cell size.
  Doors, switches and gems are sprites; the hero and foes stand on tokens.
- **Arcade verdicts** open with a drawn tick, cross or dot instead of an emoji.
- **The certificate is paper worth printing:** an engraved double border, the
  logo, a gold seal, a date and signature line, and one chip per grade passed.
- **Grade headings in the sidebar carry their own progress line**, gold once
  the grade is complete. Celebrations slide in at the edge instead of covering
  the lesson.

Gradients never stand alone: every gradient button and banner sits on a solid
`background-color`, so the contrast checks below measure a real color.

### Fifteen looks for the editor, none of them earned

Classic Dark, Midnight, Paper, Synthwave and Phosphor, plus Solarized Dark and
Light, Dracula, Nord, Gruvbox, Monokai, One Dark, Cobalt, Amber CRT and
Commodore. All available from the first minute — a color scheme is comfort, not
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
own opacity into its text color, and additionally checks that both token blocks
declare the same names and that all fifteen editor themes read.

The sampled version passed while ten real failures were live, including the
ghost coach at 1.59:1 and the Paper theme rendering HTML attributes at 1.40:1.
The sweep is the one that finds them.

## On a phone

The phone is a first-class layout, not a narrowed desktop.

- Run takes you to the Result tab: the button lives on the Code tab and what it
  made lives on Result, so pressing it switches for you.
- Two deliberate header rows — who you are and how far you have got, then the
  actions sharing the width evenly — instead of a ragged wrap.
- The tab bar pads past the home indicator (`env(safe-area-inset-bottom)`),
  frosts what scrolls under it, and marks the active tab with a rule rather than
  a color change alone. `viewport-fit=cover` and a `theme-color` that follows
  the light/dark toggle, so the browser's own chrome matches the page.
- The action row sticks to the bottom of the editor column: **Run** is always
  under a thumb, on every lesson, without scrolling.
- Nothing tappable is under 34px. The lesson crumb drops its repeated grade
  subtitle to earn its one line. Code samples wrap instead of hiding behind a
  sideways scroll.

## Features

- The preview changes only when you press Run, never while you type; the
  Quest board grows to fill the preview, and the Quest board and the Puzzle
  Vault play their sounds through the page, so the Run click unlocks them. JS lessons enforce the house rule —
  *working it out is not showing it* — via the universal `.textContent =` check
  plus a `new Function` syntax gate with friendly error rewrites.
- **Kindergarten to Grade 3 are told to press Run.** Young learners type the
  answer, watch the page change, and wait. So in those four grades, once typing
  pauses and the code would pass, the line under the buttons says *Finished?
  Press the green Run button*, and Run pulses until it is pressed (on a phone,
  a bubble sits on the button itself). Nothing is graded until Run is pressed,
  and Terminal lessons, where Enter runs each line, are left alone.
- The favicon is the Code Lab mark, embedded like everything else: SVG for
  current browsers, a PNG fallback, and an iPhone/iPad home-screen icon.
- **Give me a lead** reveals the answer in 4 word-snapped steps (scaffold, don't solve).
- **Ask a question**: offline keyword-matched answer bank (~230 entries).
- **Free play** sandbox (self-saving, uncheckable, unbreakable).
- Per-grade redo buttons, REMEMBER strip per language, reading level that
  "ages up" with the grades.
- Readable in both themes: every sampled piece of text meets WCAG AA contrast,
  and the test suite computes the real ratios from rendered styles so it cannot
  quietly regress. The coach's verdict is a live region, and the drill announces
  each question and verdict to a screen reader.
- **Runs on Mac, Windows, Chromebooks, iPad and phones.** Every shortcut takes
  Command as well as Ctrl, and the hints on screen name the key your machine
  has (⌘+Enter on a Mac, Ctrl+Enter elsewhere). The script stays inside what
  Safari 15.4 and later can read: it parses as ES2020, and it uses no regex
  lookbehind, which older Safari rejects in a way that stops the whole page.

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
Puzzle Vault, the Terminal) and `lang:'py'` bypass the JavaScript branch of
`runCheck` entirely, because that branch insists on a `screen.textContent =`
line, which is right for a page and wrong for a level, a song, a puzzle and a
`print()`. They are graded by running them: the engine's own result is a better
error than anything a regex could say about it. `normRes` skips the DOMParser
for both, and `stylePass` is replaced by `pyStyle` for Python, because the
brace-counting indent check calls every correctly indented Python program badly
indented. The `arc` lessons also get a JavaScript parse before the engine sees
them, so a missing bracket is explained in the coach's English — except
`kind:'shell'`, which is not JavaScript and skips it: `echo "<h1>Hi</h1>" >
page.html` is a perfectly good line of shell and a syntax error in anything
else.

**"Complete that last line" is not advice.** Someone who stops typing after a
comma stops *because* they do not know what comes next, so telling them to
finish the line names the one thing they are stuck on and calls it the fix.
`CALL_PARTS` lists what each room's functions are given, in order, and
`whatComesNext` walks back to the bracket that is still open, counts the pieces
already supplied and says which one is due: *makeBeat() is given 4 things inside
the brackets, separated by commas. You have typed 1 of them, so next comes which
track — a number from 1 to 8.* Only fixed-arity calls are listed, because a
function that takes any number of arguments would be counted wrong; everything
else falls back to a sentence per character — what a `,`, a `(`, a `.`, an `=`
or an `&&` was promising when the code stopped. The same sentence is what the
preview panel shows, so the board and the coach never disagree.

The half of that fix that should have come first: the decoder's operator and
punctuation pass ran on JavaScript lessons only, which left the Sound Room —
where every line is four pieces separated by commas — with no entry for the
comma at all, and Quest and Python in the same position. It now runs on those
too. Not on the Terminal: `ls -la` is not a subtraction.

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
The Puzzle Vault lessons promise that particular naive answers fail particular hidden
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
It also reports emoji, whose CSS color is not what you see; the sweep skips
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
plus the four arguments of `makeBeat` color-matched to an explanation of each.
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

**Font credits:** Inter (Rasmus Andersson), Fraunces (Undercase Type) and
JetBrains Mono (JetBrains) are embedded under the SIL Open Font License 1.1,
taken from their Fontsource packages.
