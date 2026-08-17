# Week 4 — Reading Real Code

## The big idea

Professional programmers spend far more time *reading* code than writing it. This week you learn the pro's skill: opening a 1,171-line file you didn't write (`proxy/app.py`) and, instead of drowning, building a map. By Friday you will be able to explain what this server does, section by section.

**The secret:** you never read real code top-to-bottom like a novel. You read it like a *newspaper* — headlines first, then the stories you care about.

## Step 1: Read the imports (the guest list)

The top of any Python file tells you who's invited:

```python
import hmac, json, logging, os, re, time      # Python's built-in toolbox
from collections import defaultdict, deque    # fancier built-in containers
import requests                                # third-party: makes HTTP calls OUT
from flask import Flask, jsonify, request      # third-party: receives HTTP calls IN
```

Just from the guest list you can infer: *this program receives web requests (Flask) and makes web requests (requests), deals in JSON, and keeps logs.* You learned that in 10 seconds without reading a single function.

**New idea — modules:** `import os` loads a *module* — someone else's file of functions you can use. `os.environ.get(...)` means "the `get` function in the `environ` area of the `os` module." Dots are postal addresses.

## Step 2: Read the constants (the settings panel)

```python
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
PEXELS_API_KEY    = os.environ.get("PEXELS_API_KEY", "")
APP_KEY           = os.environ.get("APP_KEY", "")
ANTHROPIC_MODEL   = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6")
ANTHROPIC_URL     = "https://api.anthropic.com/v1/messages"
```

**Environment variables** are the grown-up way to handle secrets: instead of writing the API key *in the code* (where it would be pushed to GitHub and stolen within hours — this genuinely happens), the code asks the *server's environment* for it at startup. Same code, different secrets per machine. ALL_CAPS names are a convention meaning "set once, never changed."

## Step 3: Skim the headlines — every `def`

Run this (yes, using the terminal as a reading tool is a pro move):

```bash
grep -n "^def \|^@app" proxy/app.py
```

You'll get the file's table of contents. Group what you see:

| Section | Functions | Job |
|---------|-----------|-----|
| Security & rate limiting | `_hit`, `_check_auth`, `_client_ip` | bouncers |
| Talking to Claude | `_call_anthropic`, `_extract_json`, `_is_model_rejection` | the phone line to the AI |
| Prompt building | `_build_prompt`, `_build_substitute_prompt`, `_custom_macro_fragment` | writing the AI's instructions |
| Cleanup crew | `_normalize_recipe`, `_normalize_ingredient`, `_coerce_amount`, `_coerce_float` | tidying the AI's answers |
| The endpoints | `api_recipe`, `api_substitute`, `api_identify_ingredients`, `api_photo`, `healthz` | the restaurant's menu |

Two naming conventions doing heavy lifting:

- **Leading underscore** (`_build_prompt`): "private — a kitchen helper, not on the menu." Python doesn't enforce it; it's a note between programmers.
- **`@app.post("/api/recipe")`** above a function is a **decorator** — for now, read it as a label: *"Flask, when a POST request arrives at /api/recipe, run this function."* Week 6 goes deeper.

## Step 4: Trace ONE story end to end

The core flow of the whole app, in plain English. The app asks for a recipe →

1. **`api_recipe()`** receives the request. First the bouncers: `_check_auth` (is the app key right?), `_hit` (is this caller spamming us? — rate limiting), then validation (`if not isinstance(ingredients, list)...` — did they even send ingredients?).
2. **`_build_prompt(payload)`** writes a detailed instruction letter to Claude using f-strings: the ingredients, cuisine, macro targets, and — crucially — *the exact JSON shape to answer in*.
3. **`_call_anthropic(messages)`** mails the letter: an HTTPS POST to `api.anthropic.com` with the API key in a header. It even retries with fallback models if one is retired (read `_model_chain` — that's real-world defensive programming born from an actual outage; see the git history).
4. **`_extract_json(text)`** opens Claude's reply and digs the JSON out of it (AI sometimes wraps answers in prose — this function is the "just give me the recipe" tongs).
5. **`_normalize_recipe(recipe)`** is the cleanup crew: coerces amounts to numbers, fills missing fields with defaults, makes sure every ingredient is a proper dict. **Never trust input — even from an AI.**
6. `jsonify(recipe)` sends the tidy result back to the app.

Sketch this as 6 boxes with arrows in your journal, from memory, after reading. That diagram *is* understanding.

## New concepts you'll bump into (30-second versions)

- **`try` / `except`** — "attempt this; if it blows up, do that instead of crashing." A net under the trapeze. Week 11 covers it fully; for now just recognize the shape.
- **Type hints** — `def _extract_json(text: str) -> dict:` — the `: str` and `-> dict` are *labels for humans and tools*: "text should be a string; I return a dict." Python doesn't enforce them; they're documentation that lives in the code.
- **Tuples** — `return False, jsonify(...)` returns *two* values at once, packed like `(a, b)`. The caller unpacks: `ok, err = _check_auth()`.
- **`defaultdict` / `deque`** — dictionaries/lists with superpowers, used here for the rate limiter. Skim, don't sweat.

## Break It Lab (read-only edition)

No sabotage this week — instead, *prediction training*:

1. Predict: what does `/healthz` return when `PEXELS_API_KEY` is unset? Then read `healthz()` and check yourself.
2. Predict: what happens if the app sends an empty ingredients list? Then trace `api_recipe()`'s early lines and find the exact line that rejects it.
3. Find the number `MAX` requests per hour allowed (read `_hit` and where it's called). Journal why a public server needs this.

## Checkpoint quiz

1. Why are API keys read from environment variables instead of written into the code?
2. What does a leading underscore on a function name signal?
3. In one sentence each: what do `_build_prompt`, `_call_anthropic`, and `_normalize_recipe` do?
4. Why does the server clean up (normalize) Claude's response instead of passing it straight to the app?
5. What tool did we use to get a "table of contents" of a big file?

<details><summary>Answers</summary>

1. So secrets never enter the codebase/GitHub; each machine supplies its own at runtime.
2. "Private helper — for internal use, not part of the public menu."
3. Writes Claude's instruction letter / mails it and handles retries / tidies the reply into the exact shape the app expects.
4. AI output varies; the app needs a guaranteed shape. Never trust input, even from your own AI.
5. `grep -n "^def " proxy/app.py` — searching for the headlines.
</details>

## Teach-Back

The big one: *"Explain what the Paper Plate proxy does from the moment the app asks for a recipe until it gets one back."* Six steps, no jargon — "bouncer, letter-writer, phone call, tongs, cleanup crew, reply." If you can do this smoothly, you understand more about this codebase than most people who "know Python."

## Exercises → [`exercises.md`](exercises.md)
