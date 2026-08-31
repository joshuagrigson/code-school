# Week 9 — Git & Deployment: Shipping Like a Pro

## The big idea

Code that only lives on your laptop isn't software yet; it's a diary. Two skills turn it into the real thing: **Git** (a time machine + collaboration system for code) and **deployment** (putting your server where the world can reach it). You've been *inside* a Git repo all course — this week you take the controls.

## Git in one analogy: the video game save system

- **Commit** = a named save point. You can always reload it.
- **Repository** = the whole save-file history, in the hidden `.git/` folder.
- **Branch** = a parallel save slot: experiment freely without touching your main game.
- **Remote (GitHub)** = cloud saves.
- **Push / pull** = upload / download between your machine and the cloud.

Git never overwrites history — it only adds. This is why pros are fearless: with commits, no mistake is permanent.

## The daily loop (this is 90% of real Git usage)

```bash
git status                       # what changed? ALWAYS look first
git diff                         # show me exactly what I changed, line by line
git add course/sandbox/pantry_server.py    # stage: put changes in the "to be saved" box
git commit -m "Add delete endpoint to pantry server"
git push origin my-branch        # cloud save
```

**The staging area** trips everyone up, so: think of `add` as *packing the box* and `commit` as *sealing and labeling it*. It exists so you can change five files but commit them as two separate, cleanly-labeled saves.

### Commit messages are letters to future-you

Look at this repo's actual history:

```bash
git log --oneline
# 68892b2 Add fridge camera and voice input to the web build
# 2b24e44 Survive model retirement instead of 502ing on it
```

Notice the style: present tense, says *why/what* at a human level, would make sense a year later. "fixed stuff" is a crime against your future self. Rule of thumb: finish the sentence *"If applied, this commit will…"*

## Branches: experiment without fear

```bash
git checkout -b add-stats-endpoint    # create + switch to a new save slot
# ...edit, add, commit as usual...
git checkout main                     # your main game is untouched
git merge add-stats-endpoint          # fold the experiment in when it's ready
```

**Merge conflicts** — when two branches changed the same lines, Git stops and asks a human:

```
<<<<<<< HEAD
    "model": ANTHROPIC_MODEL,
=======
    "model": "hard-coded-model",
>>>>>>> add-stats-endpoint
```

Don't panic — this is Git being *careful*, not broken. Everything between `<<<<<<<` and `=======` is one version; between `=======` and `>>>>>>>` is the other. Delete the markers, keep the right code, `git add` + `git commit`. You'll cause one on purpose in the lab so the first real one is a shrug.

## Time travel and rescue commands

```bash
git log                     # history
git checkout -- file.py     # discard uncommitted changes to a file (careful — really gone)
git stash                   # pocket all uncommitted work; git stash pop to retrieve
git revert <hash>           # new commit that undoes an old one (safe, history preserved)
```

The meta-rule: **commit early, commit often.** Small commits are cheap insurance; a day of uncommitted work is a day you can lose.

## Deployment: Render, and how the proxy actually ships

The proxy runs on **Render** — a service that watches this GitHub repo and re-runs the server for you. The whole modern deployment story in five steps:

1. You `git push` to GitHub.
2. Render notices (a *webhook* — GitHub literally sends Render an HTTP POST; Week 5 knowledge, everywhere).
3. Render builds a fresh machine: installs `proxy/requirements.txt` — this file is *why* pinning dependencies matters; it's the packing list for the new machine.
4. It launches the app per `proxy/render.yaml` (read it — it's short, and now legible to you: env vars, start command, health check path).
5. Traffic flows to the new copy; `/healthz` tells Render the new copy is alive. **That's** why health endpoints exist — machines checking on machines.

Secrets (`ANTHROPIC_API_KEY` etc.) are typed into Render's dashboard, never committed — completing the environment-variable story from Week 4.

### What "the cloud" is

A computer in a warehouse, rented by the hour, with a public address. Nothing more mystical than that. `localhost:8080` versus `paper-plate.onrender.com` is the same Flask app with a different audience.

### The static side: the PWA

The `web/` app needs no Python at all — HTML/CSS/JS files served as-is ("static hosting"). Read `web/sw.js` (52 lines): a **service worker** that caches files so the app opens offline. Skim `web/manifest.json` — the paperwork that makes "Add to Home Screen" work. PWA = progressive web app = website wearing an app costume.

## Break It Lab

Do these in a scratch branch (`git checkout -b lab-week9` — that's the point!):

1. Edit two files, stage only one, commit. Run `git status` — see the leftover. This is staging, understood forever.
2. Make a bad edit to any file, then rescue it with `git checkout -- <file>`.
3. **Cause a merge conflict on purpose:** on `lab-week9`, change a line in `course/journal.md`; switch to a second branch off main, change the *same line* differently, then merge one into the other. Resolve it. Screenshot your first conflict for posterity.
4. `git log --oneline` and `git show <hash>` an old commit from before the course. You're reading the app's archaeology.

## Checkpoint quiz

1. Working directory → staging → commit: describe with the packing-box analogy.
2. Why branch instead of editing main directly?
3. What is a merge conflict, actually? Whose fault is it?
4. Trace a `git push` to a live server on Render — the five steps.
5. Why does `requirements.txt` exist?

<details><summary>Answers</summary>

1. Edit files (workbench) → `add` packs chosen changes into the box → `commit` seals and labels it into history.
2. Experiments in a parallel slot can't break the working version; main stays always-shippable.
3. Two branches edited the same lines; Git refuses to guess and asks a human. Nobody's fault — it's a feature.
4. Push to GitHub → webhook pings Render → fresh machine installs requirements → starts app per render.yaml → healthz confirms, traffic switches.
5. It's the packing list letting any fresh machine (Render's, a teammate's) install the exact same dependencies.
</details>

## Teach-Back

Explain Git's save-system analogy AND the push-to-deployed-in-five-steps story. If your listener walks away understanding why "it works on my machine" is a joke with a solution, you've done it.

## Exercises → [`exercises.md`](exercises.md)
