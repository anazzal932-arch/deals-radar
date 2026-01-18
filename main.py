from fastapi import FastAPI
import feedparser
import re

app = FastAPI()

KEYWORDS = ["دينار", "JD"]

@app.get("/")
def home():
    return {"status": "Smart Deals Radar 🛰️ (Google RSS Mode)"}

def google_rss_search(query: str):
    url = f"https://news.google.com/rss/search?q={query}+عرض+دينار+الأردن"
    feed = feedparser.parse(url)

    deals = []

    for entry in feed.entries:
        text = entry.title + " " + entry.get("summary", "")
        price_match = re.search(r"(\d+(\.\d+)?)\s?(دينار|JD)", text)

        if price_match:
            deals.append({
                "المنتج": query,
                "السعر": float(price_match.group(1)),
                "المصدر": entry.source.title if "source" in entry else "Google",
                "العنوان": entry.title,
                "الرابط": entry.link
            })

    return deals

@app.get("/best-deal")
def best_deal(query: str = "سكر"):
    deals = google_rss_search(query)

    if not deals:
        return {
            "المنتج": query,
            "النتيجة": "❌ لا يوجد عروض حالياً"
        }

    best = min(deals, key=lambda x: x["السعر"])

    return {
        "المنتج": query,
        "أفضل عرض 🏆": best,
        "عدد العروض التي تم فحصها": len(deals)
    }
