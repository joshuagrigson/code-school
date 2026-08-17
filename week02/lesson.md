# Week 2 — Decisions and Repetition

## The big idea

Last week's programs were straight roads: step 1, step 2, done. Real programs have **forks in the road** (decisions) and **laps around the track** (repetition). Master these two and you can express almost any logic that exists in software.

## Decisions: `if` / `elif` / `else`

Think of a bouncer at a club with a checklist:

```python
age = 20
if age >= 21:
    print("Come on in")
elif age >= 18:
    print("Sorry, 21 and over tonight")
else:
    print("Definitely not")
```

Three rules that trip up every beginner:

1. **The colon `:`** ends the condition line. Forget it → `SyntaxError`.
2. **Indentation is the law.** The indented lines are what happens *if* the condition is true. Python uses indentation the way English uses paragraph structure — it's not decoration, it's meaning. Use 4 spaces, always.
3. **Only one branch runs.** Python checks top to bottom and takes the *first* true door.

### Comparisons and combinations

```python
==   # equal? (two! one = is "put into", remember)
!=   # not equal?
<  <=  >  >=
and  or  not
```

```python
if cuisine == "italian" and servings > 4:
    print("Big pasta night")
```

**Truthiness** — Python treats some values as automatically false: `0`, `""`, `[]`, `None`. So real code often reads:

```python
if not ingredients:
    return error("No ingredients given")
```

Plain English: "if the ingredients list is empty, bail out." The real proxy does exactly this — look in `proxy/app.py` in `api_recipe()`:

```python
if not isinstance(ingredients, list) or not ingredients:
```

That's a bouncer checking IDs on incoming requests.

## Repetition 1: `for` loops — "do this for each item"

```python
ingredients = ["chicken", "rice", "spinach"]
for item in ingredients:
    print(f"Prepping the {item}")
```

Read it as English: *for each item in ingredients, do the indented stuff.* The variable `item` is a temporary box that holds each element in turn.

Counting loops use `range`:

```python
for i in range(5):    # 0, 1, 2, 3, 4  (starts at 0, stops BEFORE 5)
    print(i)
```

Why start at 0? Programmers count floors like Europeans: the ground floor is 0. It feels weird for two weeks, then it's forever natural.

## Repetition 2: `while` loops — "keep going until"

```python
attempts = 0
while attempts < 3:
    password = input("Password? ")
    if password == "secret":
        print("Welcome!")
        break            # break = leave the loop immediately
    attempts = attempts + 1
```

`for` when you know *what collection* you're walking through; `while` when you know *what condition* keeps you going. `break` exits early; `continue` skips to the next lap.

**Infinite loop warning:** if the `while` condition can never become false, your program runs forever (Ctrl+C to rescue). Every `while` needs something inside that moves toward the exit.

## Building things up in a loop (the accumulator pattern)

The single most common loop shape in all of programming:

```python
total = 0                       # start empty
for price in [4.99, 2.50, 7.25]:
    total = total + price       # add each piece
print(f"Grocery total: ${total:.2f}")
```

Start with an empty box, add to it each lap, use it at the end. You'll see this pattern hundreds of times, including in this repo.

## Nesting: forks inside laps

```python
for item in ["chicken", "tofu", "beef", "tempeh"]:
    if item in ("tofu", "tempeh"):
        print(f"{item}: vegetarian ✓")
    else:
        print(f"{item}: meat")
```

Each level of meaning gets one more level of indentation. If you're 4+ levels deep, there's usually a cleaner way (Week 3 fixes this with functions).

## Break It Lab

1. Write an `if` without the colon. Read the error.
2. Indent one line of a loop body with 3 spaces instead of 4 (mixed with a 4-space line). Meet `IndentationError`.
3. Write `if x = 5:` instead of `==`. Python catches this one for you — read what it says.
4. Write a `while True:` loop with no `break`, run it, and rescue yourself with Ctrl+C. Every programmer has done this. Welcome to the club.

## Checkpoint quiz

1. What's the difference between `=` and `==`?
2. What does `range(3)` produce?
3. When do you pick `while` over `for`?
4. What does `if not ingredients:` check, in plain English?
5. What does `break` do?

<details><summary>Answers</summary>

1. `=` puts a value into a box; `==` asks "are these equal?" and answers True/False.
2. The numbers 0, 1, 2 (starts at 0, stops before 3).
3. When you don't know how many laps — you loop until a condition changes.
4. "If the ingredients box is empty (or None) — i.e. we got nothing usable."
5. Immediately exits the current loop and continues after it.
</details>

## Teach-Back

Explain: *"How does a program make a decision, and how does it repeat work?"* Use the bouncer and the laps-around-a-track analogies. Bonus points for explaining why indentation matters in Python.

## Exercises → [`exercises.md`](exercises.md)
