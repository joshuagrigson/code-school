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

### Stretch goal
`weather.py`: use `https://api.open-meteo.com/v1/forecast?latitude=X&longitude=Y&current_weather=true` (no key needed) to print your current temperature. Dig the value out of the nested JSON yourself.
