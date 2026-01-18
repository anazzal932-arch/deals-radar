from fastapi import FastAPI
import feedparser
import re
import urllib.parse

app = FastAPI()

@app.get("/")
def home():
    return {"الحالة": "الرادار الذكي نشط 🛰️", "نصيحة": "جرب /best-deal?query=سكر"}

def google_rss_search(query: str):
    # ترميز البحث للغة العربية 🛠️
    encoded_query = urllib.parse.quote(f"{query} عروض الأردن")
    url = f"https://news.google.com/rss/search?q={encoded_query}&hl=ar&gl=JO&ceid=JO:ar"
    
    feed = feedparser.parse(url)
    deals = []

    for entry in feed.entries:
        # البحث في العنوان والوصف لزيادة فرص الصيد 🎣
        full_text = entry.title + " " + entry.get("summary", "")
        
        # محاولة استخراج السعر 💰
        price_match = re.search(r"(\d+(\.\d+)?)\s?(دينار|JD|JOD)", full_text)
        price = float(price_match.group(1)) if price_match else None

        deals.append({
            "العرض 🛒": entry.title,
            "السعر المستخرج 💸": price if price else "راجع الرابط",
            "المصدر 🏛️": entry.source.title if hasattr(entry, 'source') else "جوجل",
            "الرابط 🔗": entry.link
        })
    return deals

@app.get("/best-deal")
def best_deal(query: str = "سكر"):
    results = google_rss_search(query)
    if not results:
        return {"المنتج": query, "النتيجة": "❌ لم يتم العثور على نتائج، جرب كلمة أخرى"}
    
    return {"البحث عن": query, "النتائج المكتشفة 🔍": results}
