from fastapi import FastAPI
import feedparser
import re
import urllib.parse

app = FastAPI()

@app.get("/")
def home():
    return {"الحالة": "الرادار الذكي جاهز 🛰️", "تعليمات": "اكتب المنتج بعد /best-deal?query="}

def clean_and_format_results(query, entries):
    deals = []
    for entry in entries:
        full_text = entry.title + " " + entry.get("summary", "")
        
        # 1. صنارة مطورة للأرقام والعملات (عربي وإنجليزي) 🎣
        price_pattern = r"([\d\u0660-\u0669]+(\.[\d\u0660-\u0669]+)?)\s?(دينار|JD|JOD|د\.أ)"
        price_match = re.search(price_pattern, full_text)
        
        price_val = "غير محدد"
        if price_match:
            # تحويل الأرقام العربية (١٥٠) إلى إنجليزية (150)
            p_str = price_match.group(1)
            translation = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
            price_val = float(p_str.translate(translation))

        deals.append({
            "المنتج 🛒": entry.title.split(" - ")[0], # تنظيف العنوان
            "السعر 💰": price_val,
            "المصدر 🏛️": entry.source.title if hasattr(entry, 'source') else "جوجل",
            "الرابط 🔗": entry.link
        })
    
    # 2. ترتيب النتائج (الأرخص أولاً) 📉
    # نضع الأسعار المحددة في البداية مرتبة من الأقل للأعلى
    sorted_deals = sorted(deals, key=lambda x: (x["السعر 💰"] == "غير محدد", x["السعر 💰"] if x["السعر 💰"] != "غير محدد" else 0))
    return sorted_deals

@app.get("/best-deal")
def best_deal(query: str = "زيت"):
    encoded_query = urllib.parse.quote(f"{query} عروض الأردن")
    url = f"https://news.google.com/rss/search?q={encoded_query}&hl=ar&gl=JO&ceid=JO:ar"
    
    feed = feedparser.parse(url)
    if not feed.entries:
        return {"خطأ": "لم أجد أي عروض لهذا المنتج حالياً ❌"}

    results = clean_and_format_results(query, feed.entries)
    
    return {
        "المنتج المستهدف 🎯": query,
        "إجمالي العروض المكتشفة 🛰️": len(results),
        "قائمة العروض مرتبة 📋": results
    }
