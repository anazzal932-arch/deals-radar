from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

# سنضع عدة أهداف للرادار لزيادة فرص الصيد 🎯
STORES = [
    {"name": "إكسترا الأردن", "url": "https://www.extra-jordan.com/ar/offers"},
    {"name": "كارفور الأردن", "url": "https://www.carrefourjordan.com/mafjor/ar/c/NJO1000000"}
]

@app.get("/")
def home():
    return {"status": "الرادار جاهز", "message": "استخدم مسار /deals للصيد 🎣"}

@app.get("/deals")
def get_deals():
    results = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    # الرادار سيمر على الأهداف واحداً تلو الآخر
    for store in STORES:
        try:
            response = requests.get(store["url"], headers=headers, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                # البحث عن أي عناوين عروض
                tags = soup.find_all(['h2', 'h3'])
                for tag in tags:
                    text = tag.get_text(strip=True)
                    if len(text) > 10:
                        results.append({"المحل": store["name"], "العرض 🏷️": text})
            else:
                results.append({"المحل": store["name"], "الحالة ⚠️": f"خطأ {response.status_code}"})
        except:
            results.append({"المحل": store["name"], "الحالة ⚠️": "تعذر الاتصال"})

    return {
        "تقرير الرادار 🛰️": "تم الفحص",
        "الصيد 🎣": results if results else "لم يتم العثور على نصوص واضحة حالياً"
    }
