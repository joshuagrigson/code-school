# Week 5 — The Web: HTTP, JSON & APIs

## The big idea

Every app you've ever used — Instagram, banking, Paper Plate — is two programs having a conversation: a **client** (the app in your hand) and a **server** (a program on a computer somewhere). This week you learn the language of that conversation: **HTTP**, and the format of the messages: **JSON**.

## The restaurant analogy (memorize this one)

- **You** = the client (the app)
- **The waiter** = HTTP (carries requests and responses; doesn't cook)
- **The kitchen** = the server (does the work)
- **The menu** = the API (the list of things you're allowed to ask for, and how)
- **The order ticket** = the request (structured, not freeform)
- **The plated dish** = the response

**API** = Application Programming Interface. Scary name, simple idea: *the published menu of requests a server accepts.* The Paper Plate proxy's menu is literally the endpoint table in the repo's README.

## Anatomy of an HTTP request

```
POST /api/recipe HTTP/1.1
Host: paper-plate.onrender.com
Content-Type: application/json
X-App-Key: pp_secret123

{"ingredients": ["chicken", "rice"], "servings": 2}
```

Four parts:

1. **Method** — the verb. `GET` = "just reading, changing nothing" (fetching a page). `POST` = "here's data, do something with it" (submitting an order). There are others (PUT, DELETE) but GET and POST are 95% of life.
2. **Path** — which item on the menu (`/api/recipe`).
3. **Headers** — the envelope's metadata: what format the body is (`Content-Type`), who's asking (`X-App-Key` — Paper Plate's secret handshake). Headers are how API keys travel.
4. **Body** — the actual order (JSON). GETs have no body; POSTs usually do.

## Anatomy of the response

```
HTTP/1.1 200 OK
Content-Type: application/json

{"title": "Garlic Chicken Rice", "servings": 2, ...}
```

**Status codes** — the kitchen's one-glance verdict. Learn these cold:

| Code | Meaning | Restaurant version |
|------|---------|--------------------|
| 200 | OK | "Here's your dish" |
| 400 | Bad Request | "This order ticket makes no sense" |
| 401 | Unauthorized | "You're not on the list" (bad/missing app key) |
| 404 | Not Found | "That's not on the menu" |
| 429 | Too Many Requests | "You've ordered 50 meals this hour, slow down" |
| 500 | Server Error | "The kitchen caught fire — our fault" |
| 502 | Bad Gateway | "Our supplier (the AI) failed us" |

Rule of thumb: **4xx = the client messed up; 5xx = the server messed up.** Look in `app.py`: `jsonify({"error": ...}), 400` — the number after the comma is exactly this code.

## JSON: the universal order ticket

JSON (JavaScript Object Notation) is text that describes data. If you know Python dicts and lists, you already know JSON — it's nearly the same syntax:

```json
{
  "title": "Tacos",
  "servings": 4,
  "vegetarian": false,
  "ingredients": [
    {"item": "tortillas", "amount": 6, "unit": ""}
  ],
  "notes": null
}
```

Differences from Python that WILL bite you once each:

| Python | JSON |
|--------|------|
| `True` / `False` | `true` / `false` |
| `None` | `null` |
| single or double quotes | **double quotes only** |
| trailing commas tolerated in code | **forbidden** |

Converting (Python's `json` module):

```python
import json
text = json.dumps({"a": 1})     # dict → JSON string ("dump to string")
data = json.loads('{"a": 1}')   # JSON string → dict ("load from string")
```

The proxy does `json.loads` on Claude's reply (inside `_extract_json`) and Flask's `jsonify` is doing `dumps` for every response. The entire app economy runs on these two verbs.

## `curl` and `requests`: be the client yourself

**From the terminal** (curl is HTTP-by-hand — the pro's stethoscope):

```bash
curl https://api.github.com/zen                         # GET
curl -X POST http://localhost:8080/api/recipe \
  -H 'Content-Type: application/json' \
  -H 'X-App-Key: devkey' \
  -d '{"ingredients": ["eggs", "spinach"], "servings": 2}'
```

**From Python** (the `requests` library — same thing, programmable):

```python
import requests

r = requests.post(
    "http://localhost:8080/api/recipe",
    headers={"X-App-Key": "devkey"},
    json={"ingredients": ["eggs", "spinach"], "servings": 2},
)
print(r.status_code)   # 200 hopefully
print(r.json())        # body parsed straight into a dict
```

Now re-read `_call_anthropic` in `app.py`: it's `requests.post(ANTHROPIC_URL, headers=..., json=...)` — the proxy is *itself a client* when it talks to Anthropic. **Client and server are roles, not identities.** The proxy is a server to your phone and a client to Claude, the way a restaurant is a kitchen to you and a customer to its suppliers.

## Why does Paper Plate even have a proxy? (design lesson)

Why doesn't the iPhone app call Anthropic directly? Three reasons, all fundamental:

1. **Secrets.** The Anthropic key would have to live inside the app — and anything shipped to phones can be cracked open and the key stolen. The proxy keeps the key on a server nobody can open.
2. **Control.** Rate limiting, auth, input validation — the bouncers — can only live where users can't tamper with them.
3. **Flexibility.** Swap models, fix prompts, add fallbacks (see `_model_chain`) *without shipping an app update*.

This "thin client, smart proxy" pattern is everywhere in industry. You now know why.

## Go deeper: what we deliberately skipped

This week treats HTTP as the waiter and stops there. Below the waiter is a whole kitchen infrastructure — DNS (turning `paper-plate.onrender.com` into a numeric address), TCP (the reliable delivery trucks), TLS (the armored ones — the S in HTTPS). You don't need them to build apps, but knowing they exist makes you unshakeable in debugging and interviews. Two free reads, in order:

1. [vasanthk/how-web-works](https://github.com/vasanthk/how-web-works) — the approachable version with diagrams. Read it at the END of this week; you'll recognize most of it, and the new parts will have hooks to hang on.
2. [alex/what-happens-when](https://github.com/alex/what-happens-when) — the legendary deep-dive, from the keyboard interrupt up. Save it for after Week 8 (or Week 12); it's the interview classic "what happens when you type google.com and press Enter?" answered completely. Reading it then will be a victory lap: you'll understand nearly all of it.

## Break It Lab

Run the proxy locally (fake keys fine). With curl:

1. Wrong app key → confirm you get **401** and read which function decided that.
2. `-d '{bad json'` → confirm **400**. Whose fault, per our 4xx/5xx rule?
3. GET (not POST) to `/api/recipe` → **405 Method Not Allowed**. New code! Journal what it means.
4. Misspell the path `/api/recipes` → **404**.
You just personally caused four of the six most common errors in web development. They'll never look scary again.

## Checkpoint quiz

1. GET vs POST in one sentence each.
2. Where does an API key travel in a request?
3. 401 vs 429 vs 502 — restaurant versions.
4. Translate to JSON: `{"ok": True, "note": None}`.
5. Why is the proxy both a server AND a client?

<details><summary>Answers</summary>

1. GET reads without changing anything; POST sends data for the server to act on.
2. In a header (e.g. `X-App-Key: ...` or `x-api-key` for Anthropic).
3. "Not on the list" / "slow down, you're spamming" / "our supplier failed us."
4. `{"ok": true, "note": null}` — lowercase true, null for None.
5. It serves the phone app (server role) and calls Anthropic/Pexels (client role). Roles, not identities.
</details>

## Teach-Back

Explain the restaurant analogy end to end: client, waiter, menu, ticket, status codes. Then explain *why Paper Plate has a proxy* — if you can defend that design decision out loud, you're thinking like an engineer, not a student.

## Exercises → [`exercises.md`](exercises.md)
