# Week 4 Exercises

All in your journal or `course/sandbox/` — this week is about reading, tracing, and mapping.

### 1. The map
Draw (paper is fine, photo it into the repo if you like) the full architecture: iPhone app / web PWA → proxy on Render → Anthropic API and Pexels API. Label what travels on each arrow (JSON in, JSON out, images, keys in headers).

### 2. Function autopsy: `_extract_json`
Read `_extract_json` in `proxy/app.py` closely (it's short). In your journal answer:
- What problem is it solving? (What might Claude's raw reply look like?)
- What does it do if it can't find JSON at all?
- Why is `re` (regular expressions) imported for this?

### 3. Function autopsy: `_hit` (the rate limiter)
Read `_hit` and the `defaultdict(deque)` it uses. Explain the mechanism in plain English (hint: it's a sliding one-hour window of timestamps — like a bouncer's clipboard of entry times). Why `deque` and not a plain list? (Look up `deque.popleft` — it's fast at removing from the front.)

### 4. Trace `/api/substitute`
Without running anything, write the 5–6 step story of a substitute request the way the lesson traced `/api/recipe`. Notice how much structure the two endpoints share.

### 5. Run the real thing
```bash
cd proxy
ANTHROPIC_API_KEY=fake PEXELS_API_KEY=fake APP_KEY=devkey python3 app.py
```
In a second terminal:
```bash
curl http://localhost:8080/healthz
curl -X POST http://localhost:8080/api/recipe -H 'Content-Type: application/json' -d '{}'
```
- What status/error does the second call return, and which line of `api_recipe` produced it?
- Add the header `-H 'X-App-Key: devkey'` and empty ingredients `-d '{"ingredients": []}'` — what changes?
- (The fake Anthropic key means a real recipe call will fail at step 3 of the story — that's fine. Which error comes back? Find the code that produced it.)

### Stretch goal
Pick the function in `app.py` you understand LEAST. Copy it into `course/sandbox/`, add a `print()` after every few lines, feed it fake input, and run it. Watching data move through a function is the fastest way to understand it.
