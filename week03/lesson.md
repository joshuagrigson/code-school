# Week 3 — Functions, Lists & Dictionaries

## The big idea

This is the week you stop writing scripts and start writing *software*. Three tools:

- **Lists** — ordered collections (a shopping list)
- **Dictionaries** — labeled collections (a recipe card with named fields)
- **Functions** — named, reusable recipes for *code itself*

Every real program, including `proxy/app.py`, is basically these three things arranged tastefully.

## Lists: the shopping list

```python
ingredients = ["chicken", "rice", "spinach"]

ingredients[0]          # 'chicken'  (counting from 0!)
ingredients[-1]         # 'spinach'  (negative = from the end)
len(ingredients)        # 3
ingredients.append("garlic")     # add to the end
ingredients.remove("rice")       # remove by value
"chicken" in ingredients         # True — membership test
ingredients[0:2]        # ['chicken', 'spinach'] — a slice (start included, stop excluded)
```

Loop over one (Week 2 skills):

```python
for item in ingredients:
    print(item)
```

### List comprehensions — the pro move

A compact way to build a new list from an old one:

```python
raw = ["  Chicken ", "RICE ", " spinach"]
clean = [item.strip().lower() for item in raw]
# ['chicken', 'rice', 'spinach']
```

Read right-to-left: *for each item in raw, strip and lowercase it, collect the results.* The real proxy does exactly this to sanitize incoming ingredients — in `app.py`:

```python
ingredients = [str(i).strip() for i in ingredients if str(i).strip()]
```

Plain English: "clean up every ingredient, and drop the empty ones." One line, production-grade.

## Dictionaries: the labeled form

A list finds things by *position*; a dictionary finds things by *name* (key → value):

```python
recipe = {
    "title": "Garlic Chicken Rice",
    "servings": 2,
    "ingredients": ["chicken", "rice", "garlic"],
    "cuisine": "any",
}

recipe["title"]              # 'Garlic Chicken Rice'
recipe["servings"] = 4       # change a value
recipe["prep_minutes"] = 15  # add a new key
recipe.get("calories", 0)    # 0 — .get() gives a default instead of crashing
```

**`.get()` vs `[]`** matters: `recipe["calories"]` crashes with `KeyError` if the key is missing; `recipe.get("calories", 0)` politely hands you a fallback. Servers use `.get()` constantly because you can't trust incoming data. Count the `.get(` calls in `app.py` — there are dozens.

Loop over one:

```python
for key, value in recipe.items():
    print(f"{key}: {value}")
```

### Nesting: dictionaries all the way down

Real data is dictionaries containing lists containing dictionaries:

```python
recipe = {
    "title": "Tacos",
    "ingredients": [
        {"item": "tortillas", "qty": "6"},
        {"item": "beef", "qty": "1 lb"},
    ],
}
recipe["ingredients"][1]["qty"]   # '1 lb'
```

Read the access left to right like a postal address: recipe → its ingredients list → item at position 1 → its qty. This EXACT shape is what the Paper Plate proxy returns to the app. You now read the app's data format.

## Functions: recipes for code

A function is a named block that takes ingredients (**parameters**), does work, and hands back a dish (**return value**).

```python
def scale(quantity, servings, base_servings=2):
    multiplier = servings / base_servings
    return quantity * multiplier

scale(1.5, 6)        # 4.5   (base_servings uses its default, 2)
scale(1.5, 6, 3)     # 3.0
```

Anatomy:
- `def` — "I'm defining a recipe named..."
- parameters in parentheses — the blanks callers must fill in (`=` gives a default, making it optional)
- `return` — the output. The function *stops here* and hands the value back.

**`return` vs `print`** — the #1 beginner confusion. `print` shows a value to a *human* and gives the program nothing. `return` hands a value back to the *code* that called, so it can be stored and used. A function that only prints is a chef who describes the dish but never plates it.

```python
def add(a, b):
    print(a + b)     # shows 5, returns None

result = add(2, 3)   # prints 5, but result is None!
```

### Why functions exist (the three reasons)

1. **Don't repeat yourself.** Write once, call everywhere.
2. **Name your ideas.** `sanitize_ingredients(raw)` reads like English; forty inline lines don't.
3. **Test in isolation.** You can verify one recipe works without cooking the whole meal (Week 11 builds on this).

### Scope: what happens in a function stays in a function

```python
def cook():
    secret = "extra butter"

cook()
print(secret)     # NameError — secret only existed inside cook()
```

Variables born inside a function die when it returns. This is a feature: functions can't accidentally trample each other's boxes.

## Real-code sighting

In `proxy/app.py`, find `def _build_prompt(`. Notice it takes the request data, builds a big f-string, and `return`s it. It's a pure "take ingredients → return dish" function. You can now read its signature and know *what* it does without reading every line — that's the power of good naming.

## Break It Lab

1. Access `ingredients[10]` on a 3-item list. Meet `IndexError`.
2. Access `recipe["missing_key"]` with `[]`. Meet `KeyError`. Fix with `.get()`.
3. Write a function with a `return`, then add code after the `return` inside it. Prove it never runs.
4. Call `scale()` with no arguments. Read the `TypeError` — it tells you exactly which parameters are missing.

## Checkpoint quiz

1. Why does `["a","b","c"][3]` crash?
2. When do you reach for a dict instead of a list?
3. `print` vs `return` — one sentence each.
4. What does `data.get("cuisine", "any")` do that `data["cuisine"]` doesn't?
5. What is `[x * 2 for x in [1, 2, 3]]`?

<details><summary>Answers</summary>

1. Positions are 0, 1, 2 — there is no position 3. Off-by-one strikes again.
2. When items have *names/labels* rather than just an order — a form, not a queue.
3. `print` displays to a human and returns nothing; `return` hands a value back to the calling code.
4. Returns `"any"` instead of crashing when the key is absent.
5. `[2, 4, 6]`.
</details>

## Teach-Back

Explain: *"What's the difference between a list and a dictionary, and what is a function?"* Shopping list vs. recipe card, and the recipe-for-code analogy. If your listener could then guess what `_build_prompt(payload)` does, you nailed it.

## Exercises → [`exercises.md`](exercises.md)
