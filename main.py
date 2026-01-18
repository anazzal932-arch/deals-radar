from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import re

app = FastAPI()

# قائمة المواقع المستهدفة 🛒
STORES = [
    {"name": "عروض الأردن", "url": "https://3rodh.com/jordan-offers"},
    {"name": "لبيب عروض", "url": "https://www.labeb.com/ar/offers/jordan"}
]

@app.get("/")
def home():
    return {"status": "online", "message": "الرادار يعمل بكامل طاقته 🛰️"}

@app.get("/deals")
def get_deals():
    all_results = []
    
    # بطاقة الهوية (Headers) للتنكر كمتصفح حقيقي 🕵️‍♂️
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'ar,en-US;q=0.9',
        'Referer': 'https://www.google.com/'
    }

    for store in STORES:
        try:
            # إرسال الطلب مع الـ Headers 🚀
            response = requests.get(store["url"], headers=headers, timeout=15)
            
            if response.status_code == 200:
                # استخدام BeautifulSoup لتحليل الغابة البرمجية للموقع 🥣
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # البحث عن العناوين التي تحتوي على كلمة "عرض" أو أسعار
                elements = soup.find_all(['h2', 'h3', 'p', 'span'])
                
                for el in elements:
                    text = el.get_text(strip=True)
                    # تصفية النصوص المهمة فقط (التي تحتوي على أرقام أو كلمات عرض)
                    if any(key in text for key in ["عرض", "دينار", "JD", "JOD"]) and len(text) > 5:
                        all_results.append({
                            "المتجر 🏬": store["name"],
                            "العرض 📄": text[:100]
                        })
        except Exception as e:
            print(f"Error at {store['name']}: {e}")
            continue

    # إزالة التكرار لضمان نظافة البيانات
    unique_deals = [dict(t) for t in {tuple(d.items()) for d in all_results}]
    
    return unique_deals if unique_deals else {"message": "الرادار لم يجد عروضاً جديدة حالياً 🛰️"}
