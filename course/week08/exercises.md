# Week 8 Exercises

### 1. `counter.html`
A number display and +/− buttons. Pure DOM: find, change, listen. Bonus: disable − at zero, turn the number red above 10 with `classList`.

### 2. `pantry.html` (front-end for YOUR Week 6 server!)
Run your `pantry_server.py`. Build a page that:
- fetches and displays the pantry list on load
- has an input + "Add" button that POSTs and refreshes the list
- shows server errors (the 400/409 bodies) in a status line

If the browser blocks the request, read the console error — CORS! Fix it the way the real proxy does: `pip install flask-cors`, then `from flask_cors import CORS; CORS(app)`. Journal one paragraph on what CORS is (browser asking "is this site allowed to call this server?").

### 3. `quiz.js` — phrasebook reps
In the browser console or a Node file, translate these Python one-liners to JS and verify:
- `[x * 2 for x in [1,2,3]]`
- `", ".join(["a","b","c"])`
- `len("hello")` / `len([1,2])`
- `"YES" if score > 5 else "no"` (look up the ternary `? :`)
- `{**base, "extra": 1}` (look up spread `{...base, extra: 1}`)

### 4. Recipe card, alive
Take Week 7's `card.html` and make the data dynamic: store the recipe as a JS object, render title/ingredients/steps from it with `.map().join("")`, and add a "Scale ×2" button that doubles amounts and re-renders.

### 5. Real-app safari
In `web/index.html`'s script: list every endpoint it fetches, and find the code that runs when a fetch fails. How does the app tell the user? Compare with your error handling.

### Stretch goal
Point your `pantry.html` "Suggest dinner" button at the real local proxy's `/api/recipe` (fake keys → expect the 502; show it gracefully). If you have real API keys, plug them in and watch YOUR page get a real AI recipe. Save that screenshot forever.
