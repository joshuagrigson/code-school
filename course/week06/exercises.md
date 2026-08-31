# Week 6 Exercises

### 1. Finish `pantry_server.py`
Add to the lesson's version:
- `DELETE /pantry/<item>` — remove an item (look up Flask *path parameters*: `@app.delete("/pantry/<item>")` passes `item` into the function). 404 if absent.
- `GET /pantry/check/<item>` — returns `{"item": ..., "in_pantry": true/false}`.

### 2. Bouncer upgrade
Add app-key auth to `pantry_server.py`: a constant `APP_KEY = "devkey"`, and every route (except a `/healthz` you add) returns 401 unless header `X-App-Key` matches. Write the check ONCE as a helper function — copy the `_check_auth` idea from the real proxy, simplified.

### 3. Rate limiter lite
Add a counter: if any single endpoint gets more than 20 calls since server start, return 429. (A plain dict `{path: count}` is fine — compare with the real `_hit`'s sliding window and journal why the real one is better.)

### 4. `/api/stats` on the real proxy
Do the lesson's graduation exercise if you haven't. Then extend it: include `"pexels_key_set": bool(PEXELS_API_KEY)` — mirroring how `healthz` reports without leaking secrets. Journal: why report `bool(key)` instead of the key itself?

### 5. Client + server, both yours
Write `pantry_client.py` (using `requests`) that exercises every pantry endpoint, printing PASS/FAIL for the expected status codes — including the 401, 404, and 429 cases. Congratulations: you built and tested a full API by hand.

### Stretch goal
Add `POST /pantry/suggest` that returns 3 dish ideas based on what's in the pantry — hard-coded rules are fine (rice+beans → "burrito bowl"). In Week 10 you'll replace the rules with a real Claude call, so keep the endpoint shape clean.
