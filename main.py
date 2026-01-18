from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import re

app = FastAPI()

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "ar,en-US;q=0.9"
}

KEYWORDS = ["عرض", "خصم", "دينار", "JD"]

@app.get("/")
def home():
    return {"status": "Smart Radar Online 🛰️"}

@app.get("/best-deal")
def best_deal(query: str = "سكر"):
    google_url = f"https://www.google.com/search?q={query}+عرض+دينار+الأردن"

    r = requests.get(google_url, headers=HEADERS, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    deals = []

    for g in soup.select("div"):
        text = g.get_text(" ", strip=True)

        if any(k in text for k in KEYWORDS):
            price_match = re.search(r"(\d+(\.\d+)?)\s?(JD|دينار)", text)
            if price_match:
                deals.append({
                    "النص": text[:200],
                    "السعر": float(price_match.group(1))
                })

    if not deals:
        return {"message": "لم يتم العثور على عروض حالياً"}

    best = min(deals, key=lambda x: x["السعر"])

    return {
        "المنتج": query,
        "أفضل عرض 🏆": best
    }
