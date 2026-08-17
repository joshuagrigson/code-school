# Week 7 — HTML & CSS: The Web's Skeleton and Skin

## The big idea

A web page is a body: **HTML** is the skeleton (what exists and in what structure), **CSS** is the skin and clothing (what it looks like), and next week's JavaScript is the muscles (what it can do). Paper Plate ships a real web app in `web/index.html` — 1,243 lines of all three. This week you learn to read the skeleton and skin, and build your own.

## HTML: nested boxes with name tags

HTML is just labeled boxes inside labeled boxes:

```html
<article>
  <h2>Garlic Chicken Rice</h2>
  <p>Ready in <strong>25 minutes</strong>.</p>
  <ul>
    <li>chicken</li>
    <li>rice</li>
  </ul>
</article>
```

- A **tag** opens `<p>` and closes `</p>`; everything between is inside that box.
- Nesting = boxes in boxes. Indent to match, exactly like Python blocks.
- A handful of tags do 90% of the work:

| Tag | Job |
|-----|-----|
| `<div>` / `<section>` | generic box / labeled section |
| `<h1>`–`<h3>` | headings |
| `<p>`, `<span>` | paragraph / inline snippet |
| `<ul>`, `<li>` | list and its items |
| `<button>`, `<input>`, `<form>` | things users touch |
| `<img src="...">` | image (self-closing — no content, so no closing tag) |
| `<a href="...">` | link |

### Attributes: settings on the tag

```html
<button id="generate-btn" class="btn primary" disabled>Cook it</button>
```

- `id` — a unique name for THIS element (one per page). JavaScript's handle.
- `class` — a reusable style label (many elements can share). CSS's handle.
- Others per tag: `src`, `href`, `placeholder`, `disabled`...

### The standard skeleton

```html
<!DOCTYPE html>
<html>
<head>
  <title>Tab title</title>
  <style> /* CSS lives here (or in a linked .css file) */ </style>
</head>
<body>
  <!-- everything visible lives here -->
  <script> /* JS lives here, usually at the end */ </script>
</body>
</html>
```

`head` = paperwork about the page; `body` = the page. Open `web/index.html` and confirm the shape — head full of `<meta>` and `<style>`, body full of app, `<script>` at the bottom.

## CSS: rules of dress

CSS is a list of rules: *find elements matching this selector, apply these styles.*

```css
h2 {                       /* every h2 tag */
  color: darkgreen;
  font-size: 24px;
}
.btn {                     /* everything with class="btn" — note the dot */
  padding: 12px 20px;
  border-radius: 8px;
}
#generate-btn {            /* the one element with this id — note the hash */
  background: coral;
}
```

Three selectors carry you: **tag**, **.class**, **#id**. (Real stylesheets get fancier, but this is the load-bearing 90%.)

### The box model: everything is a rectangle

Every element is a rectangle with four layers, inside-out: **content → padding (breathing room inside) → border → margin (personal space outside)**. When "the spacing looks wrong," it's one of these. Open the browser's DevTools (right-click → Inspect), click any element, and look at the colored box diagram — it's live and it's the single best CSS learning tool ever built.

### Layout: Flexbox in five lines

Arranging boxes in rows/columns is Flexbox's job:

```css
.toolbar {
  display: flex;           /* my children line up in a row */
  gap: 12px;               /* space between them */
  justify-content: space-between;  /* spread along the row */
  align-items: center;     /* centered on the cross-axis */
}
```

Parent gets `display: flex`, children obey. Search `display: flex` in `web/index.html` — the app's toolbars and rows all do exactly this.

### Variables and dark mode (read-along, in the real app)

In `web/index.html`'s `<style>`, near the top, you'll find CSS custom properties:

```css
:root { --bg: #faf7f2; --ink: #2b2320; ... }
```

...and elements use `color: var(--ink)`. Change the variable, the whole app recolors — same DRY principle as Week 3's functions, applied to design. Journal every `--variable` you find and what it seems to control.

## Read the real app

`web/index.html` is big; use Week 4 newspaper-reading:

1. Skim structure: search for `<section`, `<header`, `id=` — list the major screens/areas in your journal.
2. Pick ONE visible piece of the app (a button, the ingredient list) and find its three layers: HTML element → CSS rules that style it → (peek ahead) the JS that wires it.
3. Change something cosmetic — a color variable, a border-radius — open the file in a browser, see it. Then `git checkout -- web/index.html` to undo (or keep it if you love it — it's your app).

## Build: your recipe card page

`course/sandbox/card.html` — from a blank file, no framework, build a page showing one recipe: title, hero image (any food URL or a local file), meta row ("serves 4 · 25 min" — flexbox), ingredient list, numbered steps. Style it: max-width container centered with `margin: 0 auto`, rounded corners, a shadow (`box-shadow: 0 2px 12px rgba(0,0,0,.1)`), hover effect on a fake "Cook it" button. Make it something you'd screenshot.

## Break It Lab

1. Delete a closing `</div>` in your card page. Reload. Note the weirdness — HTML doesn't crash, it *guesses*, which is worse. DevTools' Elements tab shows you what the browser decided you meant.
2. Give two elements the same `id`. Nothing visibly breaks — until JS next week. Journal why duplicate ids are a time bomb.
3. Set `padding: 100px` on the card and watch the box model live in DevTools.
4. Misspell a CSS property (`colr: red`). Silence. CSS ignores what it doesn't understand — the opposite of Python. Both philosophies have costs; journal one sentence on each.

## Checkpoint quiz

1. HTML vs CSS vs JS — skeleton/skin/muscles, one sentence each.
2. `id` vs `class`?
3. The four box-model layers, inside-out?
4. What does `display: flex` on a parent do?
5. What happens when CSS meets a property it doesn't recognize, vs Python meeting a name it doesn't know?

<details><summary>Answers</summary>

1. HTML = structure/content, CSS = appearance, JS = behavior.
2. `id` names ONE element (unique); `class` labels MANY for shared styling.
3. Content, padding, border, margin.
4. Lays its children out along a row (or column) with alignment/spacing controls.
5. CSS silently ignores it; Python crashes with NameError. Forgiving vs strict.
</details>

## Teach-Back

Open your `card.html` next to its code and explain to someone how three specific elements got their look — element → selector → rule. Then explain the box model with a physical object (a framed photo in a padded envelope works beautifully).

## Exercises → [`exercises.md`](exercises.md)
