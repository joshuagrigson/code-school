# Week 7 Exercises

### 1. `card.html`
Build the lesson's recipe card page. Requirements: flexbox meta row, centered max-width container, styled button with hover, at least one CSS variable you define yourself (`--accent`) and use twice.

### 2. `menu.html`
A page with THREE recipe cards in a responsive row: `display: flex; flex-wrap: wrap; gap: 16px;` on the container. Shrink the browser window — cards should wrap, not squish. Extract shared card styles into a `.card` class (DRY!).

### 3. Dark mode by hand
Add a second set of variables to `menu.html`:
```css
@media (prefers-color-scheme: dark) {
  :root { --bg: #1c1917; --ink: #f5f0ea; }
}
```
Toggle your OS dark mode and watch the page follow. This is exactly the mechanism the real `web/index.html` uses — go find its dark-mode section and compare.

### 4. Real-app safari
In `web/index.html`, locate and note line numbers for:
- the `<button>` the user taps to generate a recipe
- the CSS class that styles recipe cards
- three CSS variables and what they control
- one flexbox container and what it lines up

### 5. DevTools drills (10 min/day, seriously)
On any website: Inspect an element, change its text live, change a color, delete an element, find its box model. None of this is permanent (refresh resets) — it's a flight simulator.

### Stretch goal
Rebuild the Paper Plate landing page (`index.html` at repo root) from scratch, from memory, in your own style. Compare with the real one after. Nothing teaches like a rebuild.
