# Week 9 Exercises

### 1. Commit your course work
Your `course/sandbox/` is full of two months of programs. Branch (`git checkout -b my-course-work`), then commit it in **logical chunks** (one commit per week's work, good messages), not one giant blob. Push the branch with `git push -u origin my-course-work`.

### 2. Archaeology report
Using `git log`, `git show`, and `git log --follow proxy/app.py`, write a short history of `proxy/app.py` in your journal: three moments where it changed significantly, and (from the commit messages) why. Note especially the model-retirement commit — that's a production incident and its fix, preserved in amber.

### 3. Conflict gym
Do the Break It Lab conflict twice more until resolving one takes under two minutes and zero adrenaline.

### 4. `render.yaml` and `sw.js` annotation
Copy both files into your journal and annotate every line in your own words. They're short. If a line resists explanation, that's a search-engine trip — pros look things up constantly; the skill is knowing what to ask.

### 5. Deploy something real (optional but glorious)
Render's free tier can run your `pantry_server.py`:
- Make a tiny repo (or a folder in your branch) with `pantry_server.py` and a `requirements.txt` (`flask`, `flask-cors`).
- Follow the README's Render steps, adapted.
- Curl your pantry from your phone. Your code, on the internet, answering strangers. That's shipping.

### Stretch goal
Read about `git rebase` vs `git merge` (just the concept). Journal one paragraph: why might a team prefer one main-line history? You don't need to *use* rebase yet — knowing the tradeoff exists is the pro insight.
