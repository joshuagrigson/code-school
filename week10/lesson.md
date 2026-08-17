# Week 10 — Talking to AI: The Anthropic API

## The big idea

To your code, an AI model is just another API: POST a request, get JSON back — Week 5 skills, premium ingredient. But *what you send* matters enormously: the prompt is a program written in English, and this week you learn to write good ones, force structured output, control costs, and handle images. Paper Plate's `_build_prompt` is your worked example — it's a genuinely well-crafted production prompt.

## The API call, demystified

What `_call_anthropic` sends (simplified):

```python
requests.post(
    "https://api.anthropic.com/v1/messages",
    headers={
        "x-api-key": ANTHROPIC_API_KEY,          # auth in a header — Week 5
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    },
    json={
        "model": "claude-sonnet-4-6",
        "max_tokens": 2500,
        "messages": [
            {"role": "user", "content": "The prompt goes here"}
        ],
    },
)
```

The reply contains the model's text at `resp["content"][0]["text"]` — nested-dict digging, Week 3.

Three knobs to understand:

- **model** — bigger models are smarter and pricier; smaller are faster and cheaper. Picking the smallest model that does the job well is a real engineering skill.
- **max_tokens** — a **token** is roughly ¾ of a word; you pay per token in AND out. `max_tokens` caps the reply (cost seatbelt).
- **messages** — the conversation so far. One user message = one-shot ask. Alternating user/assistant messages = a chat with memory (the API itself remembers *nothing* between calls — "chat memory" is just resending the transcript every time. This surprises everyone once.)

## Prompt engineering: programming in English

Open `_build_prompt` in `app.py` and notice its techniques — each one earned its place:

1. **Give a role.** "You are a professional chef..." — sets tone and expertise level.
2. **Be specific about constraints.** The prompt passes servings, cuisine, macro targets as concrete numbers, not vibes.
3. **Show the exact output shape.** The prompt includes a full JSON template of the response it wants — by far the highest-leverage trick in this file.
4. **Say what NOT to do.** `avoid_titles` (don't repeat recipes), rules about units and realistic amounts. Models follow explicit negative constraints well.
5. **Handle the edges in the prompt.** Weird ingredient lists, impossible macro targets — the prompt anticipates them.

**The mindset shift:** a prompt is not a wish, it's a *spec*. Vague spec → vague output. When AI output disappoints, the pro's first move is rereading their own prompt, the way you reread your own code on a bug.

## Structured output: the "reply only in JSON" contract

AIs naturally answer in prose. Apps need data. The Paper Plate pattern (industry-standard):

1. **Prompt** demands: respond with ONLY valid JSON matching this exact template.
2. **Extract** anyway defensively: `_extract_json` digs JSON out even if the model wrapped it in "Here's your recipe!" chatter (models sometimes do, no matter how sternly told).
3. **Normalize** hard: `_normalize_recipe` coerces types, fills defaults, drops junk. The AI's reply is *user input* and gets bounced through the same distrust.

Prompt → extract → normalize. Memorize the trio; you'll build it in the exercises.

## Vision: sending images

`/api/identify-ingredients` is the fridge camera: the app sends a photo, Claude answers with the ingredient list. In the API, an image is just another content block:

```python
{"role": "user", "content": [
    {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": image_base64}},
    {"type": "text", "text": "List the food ingredients you can see. Reply with only JSON: {\"ingredients\": [..]}"},
]}
```

**Base64** = binary bytes re-spelled using only text characters so they can ride inside JSON — a shipping container for images. Read `api_identify_ingredients` and recognize the whole trio again: prompt (with image), extract, normalize.

## Resilience: when the AI supplier fails

Reread these `app.py` pieces with fresh eyes; this is what production AI code looks like:

- `_model_chain` + `ANTHROPIC_FALLBACK_MODELS` — if the configured model is retired (real incident! see `git log`), try known-good fallbacks instead of 502ing forever.
- `_is_model_rejection` — *classify* an error before deciding whether retrying can help. Retrying a bad API key: pointless. Retrying a retired model on a different model: fixes it.
- Timeouts on `requests.post(..., timeout=...)` — never wait forever for a supplier.

## Cost control (the part hobby tutorials skip)

Every call costs real money, so production AI code always has:
- **Auth** (`APP_KEY`) so only your app can trigger spending
- **Rate limits** (`_hit`) capping worst-case hourly burn
- **`max_tokens`** capping per-call burn
- **Prompt frugality** — every boilerplate word in the prompt is paid for on *every single call*

You've already read all four in this codebase. The mystery ingredient was never mysterious.

## Break It Lab (needs a real API key — a few cents total; otherwise run against fake keys and study the error paths)

1. Call the API with a wrong key. Compare the 401's *shape* with your pantry server's 401.
2. Set `max_tokens: 50` and request a full recipe. Watch it truncate mid-JSON — now you *viscerally* know why `_extract_json` must survive malformed JSON.
3. Ask for JSON without showing a template, then with one. Compare reliability across 3 runs each.
4. Set a nonexistent model name and read the error body — then reread `_is_model_rejection` and see exactly which words it's sniffing for.

## Checkpoint quiz

1. In API terms, what is "asking Claude a question"?
2. What is a token, and which two things does it govern?
3. Why does the proxy still run `_extract_json` + `_normalize_recipe` when the prompt demands pure JSON?
4. Does the API remember your last call? How do chats work then?
5. Name three cost-control mechanisms in the proxy.

<details><summary>Answers</summary>

1. An HTTPS POST to /v1/messages with the key in a header and messages in the JSON body.
2. ~¾ of a word; governs cost and the max_tokens reply cap.
3. Models don't perfectly obey — output is treated as untrusted input. Prompt → extract → normalize.
4. No — totally stateless; chat = resending the whole transcript each call.
5. App-key auth, hourly rate limiting, max_tokens caps (plus lean prompts and model choice).
</details>

## Teach-Back

Explain to someone: *"When you point the app at your fridge, what actually happens?"* Photo → base64 → proxy → prompt with image → Claude → JSON extraction → cleanup → ingredient list on screen. Every single arrow is something you now understand from primary sources.

## Exercises → [`exercises.md`](exercises.md)
