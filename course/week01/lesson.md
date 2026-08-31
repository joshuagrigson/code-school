# Week 1 — How Computers Actually Think

## The big idea

A computer is the world's fastest, most obedient, most *literal* intern. It will do exactly what you say, a billion times a second, and it will never, ever guess what you meant. Programming is learning to give instructions so precise that even this intern can't get them wrong.

A **program** is just a recipe: a list of steps, executed top to bottom, one at a time. That's it. Everything else in this course — loops, functions, servers, AI — is fancy ways of writing recipes.

## Your kitchen: the Python interpreter

Python is a language the intern speaks. Open a terminal and type:

```bash
python3
```

You get `>>>` — the *REPL* (Read, Evaluate, Print, Loop). It's a conversation: you type a line, Python answers immediately.

```python
>>> 2 + 2
4
>>> "paper" + "plate"
'paperplate'
```

Try both. Notice `+` means "add" for numbers but "glue together" for text. Same symbol, different behavior depending on the *type* of thing. Hold that thought.

## Variables: labeled boxes

A variable is a box with a label, holding one value.

```python
servings = 2
cuisine = "italian"
```

Read `=` as "put into", never "equals." `servings = 2` means *put 2 into the box labeled servings*. Later:

```python
servings = servings + 1   # take out 2, add 1, put 3 back in
```

That line is nonsense in math class and perfectly normal in programming, because `=` is an *action*, not a statement of fact.

**Real-code sighting** — open `proxy/app.py` and look near the top:

```python
APP_KEY = os.environ.get("APP_KEY", "")
```

That's just a labeled box named `APP_KEY` holding whatever text the server's environment provides. You already read your first line of production code.

## Types: what kind of thing is in the box

Python cares deeply about what *kind* of value you have:

| Type | Looks like | Real-world analogy |
|------|-----------|--------------------|
| `int` | `2` | a count of things |
| `float` | `2.5` | a measurement |
| `str` (string) | `"chicken"` | text on a label |
| `bool` | `True` / `False` | a light switch |
| `None` | `None` | an empty box, deliberately |

Why care? Because `"2" + "2"` is `"22"` (gluing text) while `2 + 2` is `4`. Half of beginner bugs are type confusion. Check any value's type with `type(thing)`.

Convert between types on purpose:

```python
int("4")      # 4
str(4)        # "4"
float("2.5")  # 2.5
```

## Strings: the type you'll use most

```python
name = "Paper Plate"
len(name)            # 11 — length, counting the space
name.upper()         # 'PAPER PLATE'
name.lower()         # 'paper plate'
f"Welcome to {name}" # 'Welcome to Paper Plate'
```

That last one is an **f-string** — a template with fill-in-the-blank slots. The real proxy builds its entire AI prompt with these. This one skill carries you far.

## Input and output

```python
print("Dinner is served")        # program talks to you
answer = input("Ingredient? ")   # you talk to program; always returns a str!
```

`input()` always gives you a *string*, even if the user types `7`. If you need a number: `int(input("Servings? "))`.

## Comments

```python
# Anything after a hash is a note for humans. Python ignores it.
```

## Write your first real script

A script is REPL lines saved in a file. Create `course/sandbox/greet.py`:

```python
name = input("What's your name? ")
dish = input("Favorite dish? ")
print(f"Hi {name}! Tonight we're making {dish} for dinner.")
```

Run it: `python3 course/sandbox/greet.py`. You are now, technically and officially, a programmer.

## Break It Lab

Do each, read the error message *out loud*, then fix it:

1. In the REPL, type `"2" + 2`. Read the `TypeError`. Fix it two ways (convert either side).
2. In `greet.py`, delete a closing quote and run it. Meet `SyntaxError`.
3. Print a variable you never created (`print(dinnner)`). Meet `NameError` — the #1 typo error you'll ever see.

Error messages are not the computer yelling at you. They're the intern saying "I got confused at exactly this line, for exactly this reason." The last line of an error is almost always the answer.

## Checkpoint quiz

1. What does `=` actually do?
2. What type does `input()` always return?
3. What is `"3" * 2`? What is `3 * 2`?
4. What's the difference between `SyntaxError` and `NameError`?
5. In `proxy/app.py`, what type of value do you think `APP_KEY` holds?

<details><summary>Answers</summary>

1. Puts the value on the right into the box (variable) named on the left.
2. `str` — always a string.
3. `"33"` (strings repeat); `6` (numbers multiply).
4. `SyntaxError`: Python can't even read your code (bad grammar). `NameError`: grammar's fine but you used a box label that doesn't exist.
5. A `str` — environment variables are always text.
</details>

## Teach-Back (3 min, no jargon)

Explain to someone: *"What is a variable, and why does the computer care whether something is text or a number?"* Use the box analogy. If you reach for a word like "datatype" without explaining it — start over.

## Exercises

Head to [`exercises.md`](exercises.md).
