from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import feedparser
import re
import urllib.parse

app = FastAPI()

# إخبار السيرفر بمكان مجلد القوالب 📁
templates = Jinja2Templates(directory="templates")

def extract_price(text):
    # صنارة البحث عن الأسعار 🎣
    price_pattern = r"([\d\u0660-\u0669]+(\.[\d\u0660-\u0669]+)?)\s?(دينار|JD|JOD|د\.أ)"
    match = re.search(price_pattern, text)
    if match:
        p_str = match.group(1)
        translation = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
        try:
            return float(p_str.translate(translation))
        except:
            return None
    return None

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    # عرض الصفحة الرئيسية
    return templates.TemplateResponse("index.html", {"request": request, "query": "ابحث الآن", "results": []})

@app.get("/best-deal", response_class=HTMLResponse)
def best_deal(request: Request, query: str = "زيت"):
    encoded_query = urllib.parse.quote(f"{query} عروض الأردن")
    url = f"https://news.google.com/rss/search?q={encoded_query}&hl=ar&gl=JO&ceid=JO:ar"
    
    feed = feedparser.parse(url)
    results = []

    for entry in feed.entries[:10]:
        price = extract_price(entry.title + " " + entry.get("summary", ""))
        results.append({
            "المنتج 🛒": entry.title.split(" - ")[0], 
            "السعر 💰": f"{price} دينار" if price else "راجع الرابط",
            "المصدر 🏛️": entry.source.title if hasattr(entry, 'source') else "جوجل",
            "الرابط 🔗": entry.link
        })
    
    # ترتيب النتائج 📉
    sorted_results = sorted(results, key=lambda x: (x["السعر 💰"] == "راجع الرابط", x["السعر 💰"]))

    return templates.TemplateResponse("index.html", {
        "request": request,
        "query": query,
        "results": sorted_results
    })
