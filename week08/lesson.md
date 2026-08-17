# Week 8 — JavaScript: Making Pages Alive

## The big idea

JavaScript is the muscles: the only language browsers run, and the reason a page can respond to taps, fetch data, and update itself without reloading. Good news: you already know programming — variables, ifs, loops, functions, dicts. This week is mostly *translation*, plus two genuinely new ideas: the **DOM** and **async**.

## Python → JavaScript phrasebook

| Idea | Python | JavaScript |
|------|--------|------------|
| variable | `x = 5` | `let x = 5;` (changeable) / `const x = 5;` (locked) |
| string glue | `f"hi {name}"` | `` `hi ${name}` `` (backticks!) |
| list | `[1, 2, 3]` | `[1, 2, 3]` (same! called an array) |
| dict | `{"a": 1}` | `{a: 1}` (called an object; quotes on keys optional) |
| function | `def f(x): return x*2` | `const f = (x) => x * 2;` (an "arrow function") |
| if | `if x > 5:` | `if (x > 5) { ... }` |
| for-each | `for item in items:` | `for (const item of items) { ... }` |
| equality | `==` | `===` (use THREE; `==` does spooky type coercion) |
| null-ish | `None` | `null` (and its weird cousin `undefined` = "never set") |
| print | `print(x)` | `console.log(x)` |

Blocks use `{ }` instead of indentation, statements end with `;`, and `console.log` output appears in DevTools' **Console** tab — your JS REPL. Open it on any page right now and try `2 + 2` and `` `hello ${1+1}` ``.

## The DOM: your HTML as a live object

When the browser loads HTML, it builds the **DOM** (Document Object Model) — your page as a giant live JavaScript object. Change the object, the page changes *instantly*. This is the heart of all front-end programming:

```html
<p id="status">Waiting…</p>
<button id="cook-btn">Cook it</button>

<script>
  const status = document.getElementById("status");   // grab the element
  const btn = document.getElementById("cook-btn");

  btn.addEventListener("click", () => {               // when clicked...
    status.textContent = "Cooking!";                  // ...change the page
    btn.disabled = true;
  });
</script>
```

Three verbs run the whole show:

1. **Find**: `document.getElementById("x")` or the more general `document.querySelector(".card")` (takes any CSS selector — Week 7 pays off immediately).
2. **Change**: `.textContent = "..."` (text), `.style.color = "red"`, `.classList.add("hidden")` (toggle CSS classes — the pro way to show/hide).
3. **Listen**: `.addEventListener("click", handlerFunction)` — "when this event happens, run this function."

That last one introduces a big idea: **you hand a function to be called later.** You don't call it (`handler`) — you *name* it (no parentheses) and the browser calls it when the event fires. Functions as hand-off-able things is JavaScript's soul.

## Async and `fetch`: ordering delivery

JavaScript can't freeze the page while waiting for a server (the whole UI would lock). So slow operations are **asynchronous**: you place the order, the page keeps living, and the result arrives later. Modern syntax makes it read almost like normal code:

```javascript
async function getRecipe(ingredients) {
  const resp = await fetch("http://localhost:8080/api/recipe", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-App-Key": "devkey",
    },
    body: JSON.stringify({ ingredients, servings: 2 }),
  });
  if (!resp.ok) {                      // resp.ok = status in the 200s
    throw new Error(`Server said ${resp.status}`);
  }
  return await resp.json();            // parse body JSON → object
}
```

Translate with what you know: this is Week 5's `requests.post(...)`, browser edition.

- `fetch(url, options)` — place the order.
- `await` — "park here until the delivery arrives (without freezing the page)."
- `async` before the function — required permission slip for using `await` inside.
- `JSON.stringify(obj)` / `resp.json()` — JS's `json.dumps` / `json.loads`.

**The rookie bug** you will write exactly once: forgetting `await` and wondering why you got `Promise {<pending>}` instead of data. A Promise is the delivery receipt, not the food. `await` trades the receipt for the food.

## Put it together: the whole front-end pattern

Every interactive app — including the real one in `web/index.html` — is this loop:

```
user event  →  read inputs from DOM  →  fetch to server  →  update DOM with result
```

```javascript
btn.addEventListener("click", async () => {
  status.textContent = "Thinking…";
  btn.disabled = true;                          // prevent double-orders
  try {
    const recipe = await getRecipe(readIngredients());
    titleEl.textContent = recipe.title;
    listEl.innerHTML = recipe.ingredients
      .map(i => `<li>${i.amount} ${i.unit} ${i.item}</li>`)
      .join("");
  } catch (err) {
    status.textContent = `Something went wrong: ${err.message}`;
  } finally {
    btn.disabled = false;                       // always re-enable
  }
});
```

New pieces: `.map()` (JS's list comprehension — transforms an array), `try/catch/finally` (Python's try/except, curly-brace edition), and the disable-while-working pattern that separates amateur UIs from pro ones.

## Read the real app

In `web/index.html`, find the `<script>` section and locate:
- the `fetch(` calls — which endpoints does the web app use?
- an `addEventListener` — which button, which handler?
- an `async` function and its `await`s
- where the recipe response gets written into the DOM

You will understand *dramatically* more of it than you expect. That feeling is 8 weeks of compounding.

## Break It Lab

1. `getElementById("typo-id")` then use the result. Meet `TypeError: ... of null` — the single most common JS error in history. Diagnosis ritual: console.log the element first.
2. Remove an `await` from a fetch chain. Inspect the Promise in the console.
3. Use `==` to compare `0 == ""` and `0 === ""` in the console. Journal why we always use `===`.
4. Throw a typo inside an event handler. Notice the page loads fine and only errors *when clicked* — runtime vs load-time errors.

## Checkpoint quiz

1. What is the DOM?
2. The three DOM verbs?
3. What does `await` do, in delivery terms?
4. JS equivalents of: f-string, `json.dumps`, list comprehension, `try/except`.
5. Why disable the button during a fetch?

<details><summary>Answers</summary>

1. The live, scriptable object version of your HTML — change it and the page changes.
2. Find (querySelector), change (textContent/classList/etc.), listen (addEventListener).
3. Trades the delivery receipt (Promise) for the actual food (value), letting the page live while waiting.
4. Backtick `${}` templates; `JSON.stringify`; `.map()`; `try/catch`.
5. Users double-click; two in-flight orders mean race conditions and double costs.
</details>

## Teach-Back

Explain the full loop — event → read DOM → fetch → update DOM — using the real app: "when I tap Cook, here's everything that happens, in the browser AND on the server." You are now describing a full-stack request. That phrase on a resume is this exact explanation.

## Exercises → [`exercises.md`](exercises.md)
