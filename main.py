from fastapi import FastAPI
import feedparser
import re

app = FastAPI()

KEYWORDS = ["عرض", "خصم", "دينار", "JD"]

@app.get("/")
def home():
    return {"status": "Smart Deals Radar 🛰️ يعمل بنجاح"}

def google_rss_search(query: str):
    feed_url = f"https://news.google.com/rss/search?q={query}+عرض+دينار+الأردن"
    feed = feedparser.parse(feed_url)

    deals = []

    for entry in feed.entries:
        text = entry.title + " " + entry.get("summary", "")

        price_match = re.search(r"(\d+(\.\d+)?)\s?(دينار|JD)", text)
        if price_match:
            deals.append({
                "العنوان": entry.title,
                "السعر": float(price_match.group(1)),
                "المصدر": entry.source.title if hasattr(entry, "source") else "Google",
                "الرابط": entry.link
            })

    return deals


@app.get("/best-deal")
def best_deal(query: str = "سكر"):
    deals = google_rss_search(query)

    if not deals:
        return {
            "المنتج": query,
            "النتيجة": "لا توجد عروض حالياً"
        }

    best = min(deals, key=lambda x: x["السعر"])

    return {
        "المنتج 🛒": query,
        "عدد العروض المكتشفة 🔍": len(deals),
        "أفضل عرض 🏆": best,
        "كل العروض 📋": deals[:5]  # أول 5 فقط
    }
