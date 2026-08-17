# Week 3 Exercises

### 1. `pantry.py`
Start with `pantry = ["rice", "beans", "salt"]`. Build a loop-driven menu: `add <item>`, `remove <item>`, `list`, `quit`. Guard `remove` so a missing item prints a friendly message instead of crashing (`in` check first).

### 2. `recipe_card.py`
Build a nested dict for your favorite real recipe: title, servings, minutes, and a list of ingredient dicts (`{"item": ..., "qty": ...}`). Then write a loop that prints it as a pretty card:
```
== Tacos (serves 4, 25 min) ==
- 6      tortillas
- 1 lb   ground beef
```

### 3. `functions.py` — write these four, test each:
- `celsius_to_f(c)` → returns Fahrenheit
- `shout(text)` → returns the text uppercased with `!!!`
- `average(numbers)` → returns the mean of a list (careful with the empty list!)
- `scale_recipe(recipe, servings)` → takes a recipe dict, returns a NEW dict with servings changed (don't mutate the original — copy with `dict(recipe)`)

### 4. `sanitize.py`
Write `clean_ingredients(raw)` that takes a messy list like `["  Chicken ", "", "RICE", None, " rice "]` and returns `["chicken", "rice"]` — stripped, lowercased, empties dropped, duplicates dropped (keep first occurrence). Then compare your approach with the one-liner in `proxy/app.py` (`str(i).strip()` comprehension). Journal: what does the real one handle that yours might not?

### 5. Real-code sighting
In `proxy/app.py`, find three functions defined with `def`. For each, write ONE sentence: what goes in, what comes out. Don't read the bodies — just signatures and return statements. This is how pros skim.

### Stretch goal
`macro_math.py`: given a list of ingredient dicts each with `protein_g`, write `total_protein(ingredients)` and `highest_protein(ingredients)` (returns the dict of the winner). No googling `max()` tricks — do it with a loop first, THEN look up `max(..., key=...)` and rewrite.
