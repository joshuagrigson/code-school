# Week 5 Exercises

### 1. JSON by hand
In `course/sandbox/`, write `me.json` describing yourself: name, age, three favorite dishes (list), and an address (nested object). Validate it:
```bash
python3 -c "import json; print(json.load(open('course/sandbox/me.json')))"
```
Break it on purpose (single quotes, trailing comma, `True`) and read each error.

### 2. `api_client.py`
Using `requests`, call a free public API and print something from it:
```python
import requests
r = requests.get("https://api.zippopotam.us/us/90210")
data = r.json()
print(data["places"][0]["place name"])
```
Then extend: ask the user for a zip code, handle a bad one gracefully (check `r.status_code` before calling `.json()`).

### 3. `proxy_client.py`
Run the proxy locally with fake keys. Write a Python script that:
- calls `/healthz` and prints whether each key is set
- posts to `/api/recipe` with your app key and prints status + body
- deliberately omits the key and prints the 401 body
This script is your first *integration test* — keep it, Week 11 upgrades it.

### 4. Status code flashcards
Without looking: write the meaning of 200, 400, 401, 404, 405, 429, 500, 502. Check yourself. Repeat until 8/8.

### 5. Read the menu
Rewrite the README's endpoint table from memory in your journal: method, path, what goes in, what comes out. Then check. An engineer who knows their API's menu cold debugs 10x faster.

### 6. Your first scraper — `scrape.py`
APIs hand you tidy JSON because the server *chose* to cooperate. Most of the web doesn't — it hands you HTML meant for eyeballs. Scraping = making requests to a normal page and digging the data out yourself:

```bash
pip install beautifulsoup4
```
```python
import requests
from bs4 import BeautifulSoup

r = requests.get("https://quotes.toscrape.com")   # a site BUILT for scraping practice
soup = BeautifulSoup(r.text, "html.parser")
for q in soup.select(".quote"):                    # CSS-style selection
    text = q.select_one(".text").get_text()
    author = q.select_one(".author").get_text()
    print(f"{text} — {author}")
```

Type it, run it, then extend: collect the quotes into a list of dicts (`{"text": ..., "author": ...}`) and `json.dump` them to a file — congratulations, you just turned a webpage into an API response by hand. Notice the shape: **fetch → extract → normalize** — the exact same trio the proxy runs on Claude's replies. Untidy sources always get this treatment.

Two ground rules that make you a good citizen: scrape only sites that allow it (check `robots.txt` and the site's terms — `quotes.toscrape.com` exists precisely for practice), and never hammer a site in a loop without a pause (you know exactly why — you built a rate limiter's worth of empathy in Week 6... coming soon).

### 7. Read: how the web actually works
Read [vasanthk/how-web-works](https://github.com/vasanthk/how-web-works) end to end (~30 min). In your journal: three things this week already taught you, and the ONE new concept (DNS? TCP handshake? TLS?) you'd most like explained — write your best current guess at how it works, to compare later.

### Stretch goal
`weather.py`: use `https://api.open-meteo.com/v1/forecast?latitude=X&longitude=Y&current_weather=true` (no key needed) to print your current temperature. Dig the value out of the nested JSON yourself. Then, the compare-and-contrast that cements this week: journal one paragraph on when you'd scrape vs. when you'd use an API, having now done both.
