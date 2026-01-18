from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

STORES = [
    {"name": "عروض لبيب", "url": "https://www.labeb.com/ar/offers"},
    {"name": "Example (اختبار)", "url": "https://example.com"},
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "ar,en-US;q=0.9",
}

KEYWORDS = ["دينار", "خصم", "عرض", "JD", "%"]

@app.get("/")
def home():
    return {"status": "Radar Online 🛰️"}

@app.get("/deals")
def get_deals():
    results = []

    for store in STORES:
        try:
            r = requests.get(store["url"], headers=HEADERS, timeout=10)

            if r.status_code != 200 or len(r.text) < 800:
                raise Exception("محتوى غير صالح")

            soup = BeautifulSoup(r.text, "html.parser")
            found = []

            for tag in soup.find_all(["h1", "h2", "h3", "p", "li"]):
                text = tag.get_text(strip=True)
                if any(k in text for k in KEYWORDS) and len(text) > 10:
                    found.append(text)

            results.append({
                "المحل 🏬": store["name"],
                "الحالة": "نجح ✅",
                "العروض": list(set(found[:8]))
            })

        except:
            results.append({
                "المحل 🏬": store["name"],
                "الحالة": "محمي / JavaScript ⚠️",
                "العروض": []
            })

    return {"Radar Report 🛰️": results}
