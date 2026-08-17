# Week 12 — Capstone: Ship a Real Feature

## The big idea

No new concepts this week. Instead, the final exam every working programmer takes weekly: **take a vague idea, turn it into a shipped feature, end to end, alone.** You'll design it, branch for it, build it across the stack, test it, and merge it. When you're done, you won't need me to tell you you're a pro — the diff will say it.

## Pick ONE feature

Choose based on what you want more reps in (or invent your own of similar size — run it past the sizing test below):

### Option A: Shopping list generator (full-stack, most complete workout)
`POST /api/shopping-list` — takes a recipe (the normalized shape you know cold) and a pantry list; returns what to buy, organized by store aisle, with quantities merged. Claude does the aisle-sorting and merging (prompt → extract → normalize trio). Front-end: a "Shopping list" button on your Week 8 pantry page (or a new page) that renders the result with checkboxes.

### Option B: Recipe history & favorites (server + front-end state)
Proxy keeps recent recipes per app key in memory (a `deque` — you studied the rate limiter, same tools). Endpoints: `GET /api/history`, `POST /api/favorite`. Front-end lists history, lets you re-open and star recipes. No AI call needed — this one is about data shaping and state.

### Option C: "What am I missing?" (vision + logic, most AI-flavored)
`POST /api/gap-check` — takes a target dish name and a fridge photo. Identifies visible ingredients (reuse the identify-ingredients approach), asks Claude what the dish needs, returns `{have: [...], missing: [...], substitutions: [...]}`. The substitution prompt already exists in the codebase as inspiration.

**Sizing test** for your own idea: touches at least one new endpoint AND some front-end; buildable in ~15 hours; you can describe the request/response JSON in five minutes. Too big is the classic capstone killer — cut scope until it fits, then cut once more.

## The professional process (follow it exactly — the process IS the lesson)

### Day 1 — Design on paper, before any code
Write `course/capstone/DESIGN.md`:
1. **One-sentence pitch.** If it needs three sentences, scope is fuzzy.
2. **The API contract.** Exact request JSON, exact response JSON, error cases with status codes. (You've read five endpoints' worth of precedent — match the house style.)
3. **The prompt draft**, if AI is involved — with the JSON template it demands.
4. **A boxes-and-arrows sketch** of the flow, Week 4 style.
5. **Out of scope list.** What you are deliberately NOT building. Pros write this down; it's what keeps week-long features from becoming month-long features.

### Day 2–4 — Build inside-out
1. `git checkout -b capstone-<name>` — everything on a branch.
2. **Pure logic first**, as plain functions with pytest tests (no Flask, no network — fastest feedback loop).
3. **Then the endpoint**, following the sacred skeleton: bouncer → validate → work → normalize → respond. Auth and rate-limit it like its siblings.
4. **Then the front-end**: event → read DOM → fetch → update DOM, with the disable-while-working pattern and honest error display.
5. **Commit at every working stage** with real messages. Aim for 6+ commits telling a story, not one monster.

### Day 5 — Adversarial testing
Attack your own feature the way the labs taught you: missing fields, wrong types, empty lists, no auth, spam (does your rate limit trip?), the AI returning garbage (test your normalizer with hand-written junk). Every hole you find: regression test, then fix.

### Day 6 — Polish and merge
- Reread your own diff (`git diff main`) line by line, as a stranger. This "review your own PR" habit is the cheapest quality tool in existence.
- Update the README's endpoint table with your new endpoint — undocumented features don't exist.
- Merge to your course branch. Push. Optionally deploy and hit it from your phone.

### Day 7 — The final Teach-Back
Record 10 minutes (voice memo or video): walk through your feature — the design, one interesting implementation choice, one bug you hit and how you diagnosed it, and what you'd do differently. This recording is your diploma. A year from now it will be either embarrassing or impressive, and both outcomes mean growth.

## Graduation checklist — the pro skills you now hold

- [ ] Read a 1,000+ line production codebase with a map-first strategy
- [ ] Explain variables, types, control flow, functions, and data structures with analogies good enough to teach
- [ ] Trace an HTTP request across client → server → third-party API and back
- [ ] Build and secure a Flask API: auth, validation, rate limiting, honest errors
- [ ] Build a front-end: DOM, events, fetch, async, error states
- [ ] Use Git fearlessly: branches, conflicts, archaeology, disciplined commits
- [ ] Explain and operate a real deployment pipeline
- [ ] Integrate an AI API with the prompt → extract → normalize contract, with cost controls
- [ ] Debug with a method instead of vibes, and write tests that make change cheap
- [ ] Take a vague idea to a shipped, tested, documented feature — alone

## Where to go from here (pick by appetite)

- **Deeper Python**: classes/OOP, generators, type checking with mypy — then read Flask's own source (you can now).
- **Real front-end**: your vanilla-JS fluency is the *best possible* foundation for React — you'll understand what it automates.
- **Databases**: your pantry lives in a list that dies on restart; SQLite + SQL is the natural next chapter, and it slots straight into Flask.
- **More AI engineering**: tool use, streaming, agents, evals. You already have the hard part — treating models as fallible suppliers behind contracts.
- **Above all: ship things.** Small, finished, deployed things. Ten shipped pantry-sized projects beat one abandoned masterpiece every time.

Now go read your `course/journal.md` from Week 1. Look how far you've come. Then go teach somebody — you're qualified now, and nothing will sharpen you faster.

*Class dismissed.* 🎓
