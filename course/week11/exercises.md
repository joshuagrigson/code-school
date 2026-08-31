# Week 11 Exercises

### 1. Test your Week 3 self
Write pytest suites for your old `clean_ingredients`, `average`, and `scale_recipe`. Minimum 4 tests each: happy, two edges, one you expect to FAIL (then fix the function — you're now finding real bugs in your own two-month-old code, which is the whole point).

### 2. Test the real proxy's pure functions
The proxy's helpers are importable:
```python
# course/sandbox/test_proxy.py — run with: python3 -m pytest course/sandbox/test_proxy.py
import sys; sys.path.insert(0, "proxy")
import app

def test_coerce_float_handles_junk():
    assert app._coerce_float("2.5") == 2.5
    assert app._coerce_float(None, default=0.0) == 0.0
```
Add tests for `_extract_json` (clean JSON, JSON wrapped in prose, no JSON at all) and `_normalize_ingredient` (a proper dict, a bare string, garbage). Reading a function *to write its tests* is the deepest read there is.

### 3. Flask's test client (no server needed!)
```python
def test_recipe_rejects_missing_key():
    client = app.app.test_client()
    resp = client.post("/api/recipe", json={})
    assert resp.status_code in (400, 401)
```
Write five endpoint tests covering the bouncer layer: missing key, bad JSON, empty ingredients, wrong method, healthz OK. Your Week 5 curl drills, immortalized.

### 4. The regression ritual
Take any bug you personally hit this course (your journal has plenty). Write the test that would have caught it. Watch it pass now. Commit it with message `Add regression test for <the bug>`.

### 5. Logging retrofit
Add `logging` to your pantry server: info on each request, warning on 4xx rejections, exception on anything unexpected. Then cause one of each and read your own logs. Journal: could you diagnose each purely from the log line?

### Stretch goal
Look up pytest's `@pytest.mark.parametrize` and rewrite your `_coerce_float` tests as one parametrized test with 8 input/expected pairs. Then look up `monkeypatch` and fake `requests.post` so you can test `_call_anthropic`'s fallback logic without a key or network. (This is real professional testing — take a whole afternoon.)
