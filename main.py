from fastapi import FastAPI
import feedparser
import re
import urllib.parse

app = FastAPI()

@app.get("/")
def home():
    return {"الحالة": "الرادار الذكي جاهز 🛰️", "تعليمات": "اكتب اسم المنتج بعد الرابط"}

def extract_price(text):
    # صنارة مطورة للأرقام والعملات (عربي وإنجليزي) 🎣
    price_pattern = r"([\d\u0660-\u0669]+(\.[\d\u0660-\u0669]+)?)\s?(دينار|JD|JOD|د\.أ)"
    match = re.search(price_pattern, text)
    if match:
        p_str = match.group(1)
        # تحويل الأرقام العربية (١٥٠) إلى إنجليزية (150) لسهولة الترتيب
        translation = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
        try:
            return float(p_str.translate(translation))
        except:
            return None
    return None

@app.get("/best-deal")
def best_deal(query: str = "زيت"):
    encoded_query = urllib.parse.quote(f"{query} عروض الأردن")
    url = f"https://news.google.com/rss/search?q={encoded_query}&hl=ar&gl=JO&ceid=JO:ar"
    
    feed = feedparser.parse(url)
    results = []

    # معالجة أول 10 نتائج فقط لتجنب الازدحام
    for entry in feed.entries[:10]:
        price = extract_price(entry.title + " " + entry.get("summary", ""))
        
        results.append({
            "المنتج 🛒": entry.title.split(" - ")[0], 
            "السعر 💰": f"{price} دينار" if price else "راجع الرابط",
            "المصدر 🏛️": entry.source.title if hasattr(entry, 'source') else "جوجل",
            "الرابط 🔗": entry.link
        })
    
    # ترتيب النتائج ليظهر السعر الأرخص أولاً
    sorted_results = sorted(results, key=lambda x: (x["السعر 💰"] == "راجع الرابط", x["السعر 💰"]))

    return {
        "الهدف 🎯": query,
        "نتائج الصيد 🎣": sorted_results
    }
