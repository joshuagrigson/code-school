# Week 11 — Errors, Debugging & Testing

## The big idea

Amateurs think pros write code that works the first time. Pros know the job is: write code, watch it fail, find out why *fast*, and build nets so it can't fail the same way twice. This week: reading errors fluently, debugging systematically, handling failure gracefully (`try/except` for real), and writing automated tests.

## Reading a traceback (bottom-up, always)

```
Traceback (most recent call last):
  File "app.py", line 561, in api_recipe
    recipe = _normalize_recipe(parsed)
  File "app.py", line 497, in _normalize_recipe
    servings = int(recipe.get("servings"))
TypeError: int() argument must be a string ... not 'NoneType'
```

Read it like a detective:
- **Last line first**: what went wrong (`int(None)` — someone passed nothing to int).
- **Second-to-last frame**: where (`line 497`).
- **The stack above**: how we got there (api_recipe called _normalize_recipe). It's the call history, oldest at top.

The traceback is not noise before the "real" error — it's a map to the crime scene. Beginners google the last line; pros read the whole map first.

## The debugging method (works on every bug you will ever have)

1. **Reproduce.** Make it fail on demand. A bug you can't reproduce, you can't fix — you can only *hope*, and hope is not engineering.
2. **Locate.** Binary-search with prints: `print("got here", variable)` at the midpoint of the suspect region; the bug is before or after; repeat. Six prints finds a bug in a thousand lines.
3. **Hypothesize → test.** "I think `servings` is None because the JSON key is missing." Prove it *before* fixing. Fixing without diagnosis is repainting a wall to cure the leak behind it.
4. **Fix, and re-run the reproduction.** Watch the same command that failed now pass.
5. **Ask: where else?** The same mistake usually has siblings.

The mindset rule: **the computer is never wrong.** It did exactly what the code says. The gap is always between what you *meant* and what you *wrote* — and finding that gap is the entire game.

## `try/except`: nets under the trapeze, done right

```python
try:
    parsed = json.loads(text)
except json.JSONDecodeError:
    return jsonify({"error": "model returned invalid JSON"}), 502
```

Rules pros follow:

1. **Catch the specific exception.** A bare `except:` catches *everything* — including your own typos — and turns loud, honest crashes into silent lies. The most expensive habit in Python.
2. **Wrap the risky line(s), not the whole function.** Small nets show exactly what you expected might fail: the JSON parse, the network call — not the arithmetic.
3. **Do something honest in the except.** Return a proper error status, log it, or re-raise. Swallowing (`except: pass`) buries evidence.

Where failure is *expected*, don't even use exceptions — use defaults: `data.get("cuisine", "any")`. Reserve try/except for genuinely risky operations: network calls, parsing outside data, file I/O. Skim `app.py` and notice its nets are exactly there — around `requests.post` and JSON parsing — never around its own logic.

## Testing: paranoia, automated

You've been testing manually all course (curl, running scripts, clicking). Automated tests are that, written down, runnable in seconds forever. With **pytest** (`pip install pytest`):

```python
# course/sandbox/test_sanitize.py
from sanitize import clean_ingredients      # your Week 3 function!

def test_strips_and_lowercases():
    assert clean_ingredients(["  Chicken "]) == ["chicken"]

def test_drops_empties_and_nones():
    assert clean_ingredients(["", None, "rice"]) == ["rice"]

def test_dedupes_keeping_first():
    assert clean_ingredients(["Rice", "rice "]) == ["rice"]

def test_empty_input_gives_empty_list():
    assert clean_ingredients([]) == []
```

Run `pytest` in that folder — it auto-finds `test_*.py` files and functions, runs each, and reports. `assert expr` means "this must be true, or the test fails."

What to test (the art):
- **The happy path** — normal input, expected output.
- **The edges** — empty list, empty string, zero, huge, duplicates, None.
- **Every bug you ever fix** — write the test that *would have caught it* first, watch it fail, then fix. The bug can never return unseen. This habit alone is half of professional quality.

Why bother, really: **tests make change cheap.** With a test suite, you can refactor `_normalize_recipe` fearlessly — run pytest, all green, ship. Without one, every change is a prayer. Tests are not homework; they're courage.

## Logging: print's grown-up sibling

`app.py` uses `logging` instead of print:

```python
logging.info("recipe request: %d ingredients", len(ingredients))
logging.exception("anthropic call failed")     # auto-includes the traceback!
```

Levels (debug/info/warning/error) let you dial verbosity without editing code, and on Render these lines become the *only* eyes you have on a live server. Deployed code with no logging is a car with no dashboard. Find three `logging.` calls in `app.py` and journal what question each would answer during an outage at 2am.

## Break It Lab (diagnosis drills)

Plant each bug in a copy of your pantry server, then find it using ONLY the method (no ctrl-Z-ing straight to the fix):

1. Change a `==` to `=` ... wait, Python blocks that. Change `>=` to `>` in a boundary check instead — the classic *off-by-one*. Find it by testing boundaries.
2. Swap two parameters at a call site (`scale(servings, qty)`). Type confusion at a distance.
3. Make a helper `return` nothing on one path (forgotten return). Track the resulting `None` back upstream from where it explodes — the crash site is downstream of the crime.
4. Add a bare `except: pass` around a broken line and observe how much *worse* silent failure is than a crash. Delete it with prejudice.

## Checkpoint quiz

1. Which end of a traceback do you read first, and what do the two ends tell you?
2. The five debugging steps?
3. Two reasons a bare `except:` is dangerous?
4. What three categories of input should a test suite cover?
5. Why logging over print on a deployed server?

<details><summary>Answers</summary>

1. Bottom: what + where. Top: the call path that led there.
2. Reproduce, locate (binary-search prints), hypothesize & verify, fix & re-test, look for siblings.
3. It hides your own typos as "handled" failures, and it turns honest crashes into silent wrong behavior.
4. Happy path, edge cases, and regressions (every fixed bug).
5. Levels you can dial, timestamps/tracebacks for free, and it's your only visibility into a remote machine.
</details>

## Teach-Back

Hand someone a printed traceback (make one!) and narrate the detective read. Then explain *why tests are courage* — the refactoring argument. If they say "oh, so tests aren't about proving it works, they're about keeping it working" — full marks, teacher.

## Exercises → [`exercises.md`](exercises.md)
