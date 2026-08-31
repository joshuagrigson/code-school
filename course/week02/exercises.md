# Week 2 Exercises

### 1. `fizzbuzz.py` (the classic interview question)
Print numbers 1–30. For multiples of 3 print `Fizz`, multiples of 5 print `Buzz`, multiples of both print `FizzBuzz`. Hint: check "both" FIRST (why? — write the answer in your journal).

### 2. `doneness.py`
Ask for a steak temperature (°F). Print rare (<130), medium-rare (130–139), medium (140–149), medium-well (150–159), or well done (160+). Test every boundary value: 129, 130, 139, 140...

### 3. `guess.py`
Pick a secret number (hard-code it, e.g. 7). Loop with `while`: ask for guesses, say "higher"/"lower", congratulate on success and report how many guesses it took.

### 4. `grocery_total.py`
Loop asking for prices until the user types `done`. Then print the count of items and the total. (Accumulator pattern + a `while` + a `break`.)

### 5. `menu_filter.py`
Given `dishes = ["carbonara", "pad thai", "tacos", "pho", "pizza", "ramen"]`, print only dishes with 5 or more letters, numbered:
```
1. carbonara
2. pad thai
...
```
Hint: keep your own counter that only advances when you print.

### 6. Real-code sighting
In `proxy/app.py`, find the function `api_recipe`. Count the `if` statements in its first ~30 lines and write one sentence in your journal about what each one is guarding against. (They're all bouncers rejecting bad requests.)

### Stretch goal
`prime.py`: ask for a number, print whether it's prime. (A number is prime if nothing from 2 up to it divides it evenly — `%` is your friend.)
