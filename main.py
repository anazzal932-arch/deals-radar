from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

# قائمة أهداف متنوعة لزيادة فرص الصيد 🎯
STORES = [
    {"name": "كارفور الأردن", "url": "https://www.carrefourjordan.com/mafjor/ar/c/NJO1000000"},
    {"name": "لبيب عروض", "url": "https://www.labeb.com/ar/offers"}
]

@app.get("/")
def home():
    return {"status": "الرادار نشط 🛰️", "instruction": "جرب مسار /deals لرؤية النتائج"}

@app.get("/deals")
def get_deals():
    final_results = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    for store in STORES:
        try:
            # نحاول الصيد من كل موقع بمهلة زمنية محددة
            response = requests.get(store["url"], headers=headers, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                # نبحث عن العناوين التي قد تحتوي على عروض
                headings = soup.find_all(['h2', 'h3'])
                deals_found = [h.get_text(strip=True) for h in headings if len(h.get_text()) > 10]
                
                final_results.append({
                    "المحل": store["name"],
                    "العروض 🛒": deals_found[:10] # نكتفي بأول 10 عروض
                })
            else:
                final_results.append({"المحل": store["name"], "الحالة ⚠️": f"كود الحالة {response.status_code}"})
                
        except Exception as e:
            # إذا فشل موقع، نسجل الخطأ وننتقل للذي يليه
            final_results.append({"المحل": store["name"], "الحالة ⚠️": "تعذر الاتصال بالموقع حالياً"})

    return {
        "تقرير الرادار 🛰️": "فحص العروض الجاري",
        "النتائج 🎣": final_results
    }
