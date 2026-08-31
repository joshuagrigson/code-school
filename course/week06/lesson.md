# Week 6 — Flask: Building Your Own Server

## The big idea

Last week you were the customer. This week you build the restaurant. **Flask** is a small Python library that turns your functions into a web server: you tell it "when someone asks for X, run this function," and it handles all the HTTP plumbing. By Friday you'll have built a server from zero AND added a real endpoint to the Paper Plate proxy.

## The smallest possible restaurant

Create `course/sandbox/hello_server.py`:

```python
from flask import Flask

app = Flask(__name__)          # open the restaurant

@app.get("/")                  # menu item: GET /
def home():
    return "Welcome to my server!"

@app.get("/about")
def about():
    return "Built during week 6."

if __name__ == "__main__":
    app.run(port=5001, debug=True)
```

Run it, then visit `http://localhost:5001` in a browser (a browser is just a GET machine with a paint department). **You are running a web server.** Same species as Google's, smaller portions.

### That `@app.get("/")` thing — decorators, demystified

A **decorator** is a label you stick on a function that registers or wraps it. `@app.get("/")` tells Flask: *"add this function to the menu, under GET /."* The function itself is normal; the decorator is the menu entry. That's genuinely all you need for this course.

`__name__ == "__main__"` translated: "only start the server if this file was run directly, not if it was imported by another file." Boilerplate; type it, move on.

## Taking orders: reading the request

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.post("/api/greet")
def greet():
    data = request.get_json(silent=True) or {}      # the order ticket, as a dict
    name = data.get("name", "stranger")             # .get with default — Week 3!
    return jsonify({"message": f"Hello, {name}!"})  # dict → JSON response
```

Three imports carry the whole framework:

- `request` — the incoming order (its JSON body, its headers `request.headers.get("X-App-Key")`, the caller's address)
- `jsonify(dict)` — plate a dict as a proper JSON response
- returning `jsonify(...), 400` — a tuple sets the status code. Sound familiar from `app.py`? It should — you've been reading this pattern for two weeks.

`silent=True` means "if the body isn't valid JSON, give me None instead of exploding" — then `or {}` swaps None for an empty dict. Defensive cooking.

## The full pattern every real endpoint follows

Every serious endpoint — including all five in `proxy/app.py` — has this skeleton. Learn it as a *shape*:

```python
@app.post("/api/thing")
def api_thing():
    # 1. BOUNCER: auth / rate limit
    ok, err = check_auth()
    if not ok:
        return err                                   # 401

    # 2. VALIDATE: never trust input
    data = request.get_json(silent=True) or {}
    items = data.get("items")
    if not isinstance(items, list) or not items:
        return jsonify({"error": "items must be a non-empty list"}), 400

    # 3. WORK: the actual job (often calling another API)
    result = do_the_thing(items)

    # 4. NORMALIZE: guarantee the response shape
    # 5. RESPOND
    return jsonify(result)
```

Bouncer → validate → work → tidy → respond. Once you see this shape, `api_recipe`'s ~50 lines stop being intimidating — they're this skeleton with real flesh.

## Build: a mini recipe API (no AI yet)

`course/sandbox/pantry_server.py` — your project for the week. A pantry API with an in-memory list:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)
PANTRY = ["rice", "beans"]                # lives in memory; resets on restart

@app.get("/pantry")
def list_pantry():
    return jsonify({"items": PANTRY, "count": len(PANTRY)})

@app.post("/pantry")
def add_item():
    data = request.get_json(silent=True) or {}
    item = str(data.get("item", "")).strip().lower()
    if not item:
        return jsonify({"error": "item is required"}), 400
    if item in PANTRY:
        return jsonify({"error": f"{item} already in pantry"}), 409   # 409 Conflict — new code!
    PANTRY.append(item)
    return jsonify({"items": PANTRY}), 201    # 201 Created — the polite POST success
```

Test it with curl and with your Week 5 `requests` skills. Note the two new status codes — your vocabulary is growing exactly the way a pro's did.

## Graduation: touch the real proxy

Add a real endpoint to `proxy/app.py`. Right after `healthz`, add:

```python
@app.get("/api/stats")
def api_stats():
    return jsonify({
        "model": ANTHROPIC_MODEL,
        "endpoints": ["/api/recipe", "/api/substitute",
                      "/api/identify-ingredients", "/api/photo"],
        "uptime_hint": "since last deploy",
    })
```

Run the proxy, curl it, see your endpoint answer *alongside* the production ones. (Decide with your own judgment: should stats require the app key? There's a defensible answer both ways — journal yours. Hint: `healthz` doesn't require it. Why might that be?)

## Break It Lab

1. Define two functions with the same route path. What does Flask do? (Read the error carefully — it's unusually helpful.)
2. Return a plain dict *without* `jsonify`. Does modern Flask cope? (Try it — you might be surprised, and now you know a piece of Flask trivia.)
3. Forget the `return` in an endpoint. What does the browser/curl get? Read the error about `None`.
4. Start the server twice in two terminals on the same port. Meet "address already in use" — a rite of passage. Fix by killing one or changing ports.

## Checkpoint quiz

1. What does `@app.post("/api/recipe")` tell Flask, in plain English?
2. What's the difference between `request` and `requests`? (Cruel, but the confusion is real.)
3. What are the 5 steps of the endpoint skeleton?
4. Why validate input when your own app is the only client?
5. What do 201 and 409 mean?

<details><summary>Answers</summary>

1. "When a POST arrives at /api/recipe, run this function and send back what it returns."
2. `request` (Flask) = the incoming order you're serving. `requests` (library) = the tool for placing your own orders to other servers. In vs. out.
3. Bouncer, validate, work, normalize, respond.
4. Because clients lie, break, and get imitated — anyone with curl can hit your URL. The server is the last line of defense.
5. 201 "created it for you"; 409 "conflicts with what already exists."
</details>

## Teach-Back

Whiteboard-style: draw the endpoint skeleton and narrate a request flowing through your pantry server. If you can improvise a *new* endpoint on the spot while explaining (`DELETE /pantry`?), you've internalized it.

## Exercises → [`exercises.md`](exercises.md)
