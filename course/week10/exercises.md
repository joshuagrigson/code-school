# Week 10 Exercises

(1–3 need an Anthropic API key — a dollar of credit covers the whole week. No key? Do 4–5 fully and write 1–3 as "dry runs": complete code, expected behavior journaled.)

### 1. `ask.py` — your first direct AI call
A CLI script: takes a question as input, POSTs to the Anthropic API with `requests` (build the call yourself — no SDK, that's the point this week), prints the answer. Read the key from an environment variable like the proxy does — never hard-code it.

### 2. `dinner_bot.py` — the structured-output trio
Ask the user for ingredients, then:
- **Prompt** with a role, constraints, and an exact JSON template (`{"title":..., "minutes":..., "steps":[...]}`)
- **Extract**: parse the reply; if `json.loads` fails, try slicing from the first `{` to the last `}` (mini `_extract_json`)
- **Normalize**: guarantee title is a string, minutes an int, steps a non-empty list — defaults if not
Print a tidy recipe card (Week 3 skills). Run it 5 times; journal any misbehavior your normalizer caught.

### 3. Pantry server, now with brains
Replace Week 6's hard-coded `/pantry/suggest` rules with a real Claude call using your trio from #2. Your own full-stack AI feature: browser → your Flask → Anthropic → browser.

### 4. Prompt surgery on the real thing
Read `_build_prompt` top to bottom. In your journal:
- List every input that shapes the prompt (payload fields).
- Find the JSON template it shows the model.
- Find two "what not to do" rules and explain why each exists (imagine the bad output that prompted it).
- Propose ONE genuine improvement (a wasted phrase, an unhandled edge, a clearer constraint). Keep it — it might be your capstone.

### 5. Cost audit
Estimate the worst-case hourly Anthropic spend a single hostile IP could cause against the deployed proxy, using the actual rate-limit numbers and max_tokens in `app.py` (rough token pricing from your notes is fine). Journal the calculation. This exercise is why the bouncers exist.

### Stretch goal
`fridge.py`: send a photo of your actual fridge (base64-encode a JPEG in Python) with an identify-ingredients prompt, then feed the result straight into your `dinner_bot.py`. You just rebuilt Paper Plate's signature feature in ~100 lines.
