# The Paper Plate Coding Class — 12 Weeks to Pro

**The one-sentence pitch:** you will learn to code by rebuilding, breaking, fixing, and extending *your own shipped app* — Paper Plate — until you understand every line in this repo well enough to teach it to someone else.

## Why this class is different

Most coding courses teach you toy examples: `print("hello world")`, a todo list, a calculator. Then you open a real codebase and feel lost, because real code has API keys, deployments, error handling, and three languages talking to each other. **This course inverts that.** The real codebase IS the textbook. By week 12 you'll understand:

- **Python + Flask** (the `proxy/` server that talks to Claude)
- **JavaScript + HTML/CSS** (the `web/` PWA)
- **HTTP and APIs** (how the app, the proxy, and Anthropic actually talk)
- **Git and deployment** (Render, service workers, real shipping)
- **AI integration** (prompting, structured output, vision)

## The teaching philosophy (read this once, it explains everything)

1. **Plain-English first.** Every concept gets a real-world analogy *before* any code. A variable is a labeled box. A function is a recipe card. An API is a restaurant waiter. If you can't picture it, you can't debug it.
2. **You can't learn to swim from a book.** Every week is ~20% reading, ~80% typing. Exercises live in `course/weekNN/exercises.md` and most of them touch real files in this repo.
3. **The Feynman rule.** Each week ends with a **Teach-Back**: explain the week's big idea out loud (to a person, a rubber duck, or a voice memo) in under 3 minutes with no jargon. If you stumble, that's the exact spot you don't understand yet. This is the single highest-leverage habit in the course.
4. **Breaking things is the curriculum.** Every week has a "Break It Lab" — you intentionally sabotage working code, observe the error, and fix it. Pros aren't people who don't get errors; they're people who've *seen* the errors before.

## Weekly rhythm (~6–8 hours/week)

| Day | Activity |
|-----|----------|
| 1–2 | Read the lesson (`lesson.md`), type along with every example |
| 3–4 | Do the exercises (`exercises.md`) |
| 5 | Break It Lab |
| 6 | Checkpoint quiz (answers at the bottom — no peeking first) |
| 7 | Teach-Back + rest |

## The 12 weeks

| Week | Title | You'll be able to... |
|------|-------|----------------------|
| 1 | How Computers Actually Think | run Python, use variables/types, read any simple script |
| 2 | Decisions and Repetition | write if/else, loops, and understand program flow |
| 3 | Functions, Lists & Dictionaries | organize data and logic like `app.py` does |
| 4 | Reading Real Code | trace the entire Paper Plate proxy line by line |
| 5 | The Web: HTTP, JSON & APIs | explain exactly what happens when the app fetches a recipe |
| 6 | Flask: Building Your Own Server | write endpoints from scratch; extend the real proxy |
| 7 | HTML & CSS: The Web's Skeleton and Skin | read/modify `web/index.html`, build a page from zero |
| 8 | JavaScript: Making Pages Alive | DOM, events, `fetch` — the language of the browser |
| 9 | Git & Deployment: Shipping Like a Pro | branch, commit, resolve conflicts, deploy to Render |
| 10 | Talking to AI: The Anthropic API | prompt engineering, structured output, vision, cost control |
| 11 | Errors, Debugging & Testing | debug systematically, write tests, handle failure gracefully |
| 12 | Capstone: Ship a Real Feature | design, build, and deploy a new Paper Plate feature end-to-end |

## Already know some programming? Start here

If you've learned basic programming elsewhere (variables, lists, functions, conditionals, loops — in any language), here's how the course lands for you:

- **Weeks 1–3 are NOT skippable, but they'll be fast.** They teach Python fundamentals; if you know the ideas from another language, expect "oh, it's `def` instead of `function`" moments constantly. Enjoy them: your second language always costs a fraction of your first.
- **Weeks 7–8 (HTML/CSS/JS) will be part review, part promotion** if you've touched web basics — they add layout (flexbox), the DOM as a system, `fetch`, and reading a 1,200-line production page. Do the exercises anyway; they're at real-app scale, not lesson scale.
- **The big new territory** is Weeks 4–6 and 9–12: servers, HTTP, Git, deployment, AI APIs, testing — the parts that make you professional.
- **Habits that matter here:** type everything by hand. When something seems confusing, suspect a defect in the material before doubting yourself — write it in the journal and fix or flag it. And working something out is not the same as showing it: that becomes `return` vs `print` (Week 3) and honest error responses (Week 6).

## Setup (do this before Week 1)

```bash
# 1. Check Python (3.9+ is fine)
python3 --version

# 2. Make a practice sandbox inside the repo (it's gitignored-safe to experiment)
mkdir -p course/sandbox

# 3. Install the proxy's dependencies so real-code weeks work
cd proxy && pip install -r requirements.txt && cd ..
```

## Rules of the road

- **Type every example by hand.** Copy-paste teaches your clipboard, not your brain.
- **When stuck for 20+ minutes, that's enough.** Look at the answer, understand it, then re-do it from scratch tomorrow. Struggle is learning; suffering is not.
- **Keep a `course/journal.md`.** One paragraph per session: what you did, what confused you, what clicked. In week 12 you'll read it back and be shocked how far you've come.

Start with [`week01/lesson.md`](week01/lesson.md). See you at pro.
