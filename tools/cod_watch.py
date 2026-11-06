"""Watch Call of Duty's patch notes and push a phone alert when MW4 gets an update.

Runs hourly from .github/workflows/cod-update-alert.yml. Standard library only.

How it decides "there's an update":
  1. Read callofduty.com/patchnotes and keep the Modern Warfare 4 links
     (new seasons, Reloaded drops, hotfix pages).
  2. Open the newest few and fingerprint the article text. Mid-season hotfixes
     are usually added *inside* an existing page ("Additional November 5
     Updates"), so a changed fingerprint counts as an update too.
  3. Compare with state.json from the last run. New link or changed text ->
     push to ntfy. The first run just records what's there and sends one
     "watcher is live" test so you know the alert reaches your phone.
"""
import hashlib
import json
import os
import re
import sys
import urllib.request

BASE = "https://www.callofduty.com"
INDEX = BASE + "/patchnotes"
GAME = re.compile(r"modern-warfare-4|mw4", re.I)
NEWEST = 3  # how many recent MW4 pages to fingerprint
STATE = os.environ.get("STATE_FILE", "state.json")
TOPIC = os.environ["NTFY_TOPIC"]


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (cod-update-alert)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "ignore")


def article(url):
    """Return (title, text) for a patch notes page, text stripped of markup."""
    html = get(url)
    m = re.search(r'<h1 class="title">(.*?)</h1>(.*?)(?:<footer|$)', html, re.S)
    if not m:
        return url, html  # page layout changed; fall back to the raw page
    body = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", m.group(2), flags=re.S)
    text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body)).strip()
    return re.sub(r"<[^>]+>", "", m.group(1)).strip(), text


def push(title, message, url):
    req = urllib.request.Request(
        "https://ntfy.sh/" + TOPIC,
        data=message.encode(),
        headers={"Title": title, "Click": url, "Tags": "video_game", "Priority": "high"},
    )
    urllib.request.urlopen(req, timeout=30).read()


def main():
    links = re.findall(r'href="(/patchnotes/(\d{4})/(\d{2})/[^"]+)"', get(INDEX))
    mw4 = sorted({(y, m, p) for p, y, m in links if GAME.search(p)}, reverse=True)[:NEWEST]
    if not mw4:
        sys.exit("No MW4 patch notes found - the page layout may have changed.")

    now = {}
    titles = {}
    for _, _, path in mw4:
        titles[path], text = article(BASE + path)
        now[path] = hashlib.sha256(text.encode()).hexdigest()

    try:
        with open(STATE) as f:
            before = json.load(f)
    except FileNotFoundError:
        before = None

    if before is None:
        push("CoD watcher is live",
             "You'll get a ping like this when Modern Warfare 4 gets a patch.",
             BASE + mw4[0][2])
    else:
        changed = [p for p in now if before.get(p) != now[p]]
        for path in changed:
            kind = "New patch notes" if path not in before else "Patch notes updated"
            push("CoD update: " + kind,
                 titles[path] + "\nYour Xbox should be downloading it now.",
                 BASE + path)
        print("changed:", changed or "nothing")

    with open(STATE, "w") as f:
        json.dump(now, f, indent=1, sort_keys=True)


if __name__ == "__main__":
    main()
