from fastapi import FastAPI
import feedparser
import re
import urllib.parse

app = FastAPI()

@app.get("/")
def home():
    return {
        "الحالة": "رادار العروض الذكي 🛰️ (وضع جوجل RSS)",
        "طريقة الاستخدام": "أضف /best-deal?query=اسم_المنتج للرابط"
    }

def google_rss_search(query: str):
    # ترميز النص العربي ليفهمه الرابط بشكل صحيح 🛠️
    encoded_query = urllib.parse.quote(f"{query} عروض الأردن")
    url = f"https://news.google.com/rss/search?q={encoded_query}&hl=ar&gl=JO&ceid=JO:ar"
    
    feed = feedparser.parse(url)
    deals = []

    for entry in feed.entries:
        text = entry.title
        # البحث عن الأسعار (مثلاً: 5 دينار أو 5.99 JD) 💸
        price_match = re.search(r"(\d+(\.\d+)?)\s?(دينار|JD|JOD)", text)

        if price_match:
            deals.append({
                "العرض 🛒": entry.title,
                "السعر 💰": float(price_match.group(1)),
                "المصدر 🏛️": entry.source.title if hasattr(entry, 'source') else "جوجل",
                "الرابط 🔗": entry.link
            })
    return deals

@app.get("/best-deal")
def best_deal(query: str = "سكر"):
    deals = google_rss_search(query)

    if not deals:
        return {
            "المنتج": query,
            "النتيجة": "❌ لا يوجد عروض حالياً في قاعدة بيانات جوجل",
            "نصيحة": "جرب كلمات أخرى مثل: زيت، دجاج، أرز"
        }

    # ترتيب العروض من الأقل سعراً للأعلى 📉
    sorted_deals = sorted(deals, key=lambda x: x["السعر 💰"])

    return {
        "المنتج المستهدف": query,
        "أفضل صيد 🏆": sorted_deals[0],
        "عروض أخرى مكتشفة": sorted_deals[1:5]
    }
