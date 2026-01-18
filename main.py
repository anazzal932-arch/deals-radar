from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

# 1. نظام روابط الطوارئ: قائمة أهداف متنوعة لضمان النتائج
STORES = [
    {"name": "كارفور الأردن", "url": "https://www.carrefourjordan.com/mafjor/ar/c/NJO1000000"},
    {"name": "لبيب عروض", "url": "https://www.labeb.com/ar/offers"},
    {"name": "إكسترا الأردن", "url": "https://www.extra-jordan.com/ar/offers"}
]

@app.get("/")
def home():
    return {"status": "الرادار الذكي يعمل", "message": "توجه إلى /deals لبدء الصيد 🗺️"}

@app.get("/deals")
def get_deals():
    final_results = []
    
    # 2. تطوير الهوية (User-Agent): التخفي كمتصفح حقيقي لتجاوز الحظر
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'ar,en-US;q=0.9',
        'Referer': 'https://www.google.com/'
    }

    for store in STORES:
        try:
            # محاولة الاتصال مع مهلة زمنية (Timeout) لتجنب التعليق
            response = requests.get(store["url"], headers=headers, timeout=12)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # 3. تحليل الهيكل: البحث عن كلمات مفتاحية (دينار، عرض، خصم)
                deals_list = []
                # نبحث في العناوين والفقرات (h2, h3, p)
                for element in soup.find_all(['h2', 'h3', 'p']):
                    text = element.get_text(strip=True)
                    if any(key in text for key in ["دينار", "خصم", "JD", "%", "عرض"]):
                        if len(text) > 8:
                            deals_list.append(text)
                
                final_results.append({
                    "المحل 🏬": store["name"],
                    "الحالة ✅": "تم الصيد بنجاح",
                    "العروض 🛒": list(set(deals_list[:10])) # إزالة التكرار وأخذ أول 10 عروض
                })
            else:
                final_results.append({"المحل": store["name"], "الحالة ⚠️": f"خطأ {response.status_code}"})
                
        except Exception as e:
            # معالجة الأخطاء الذكية: تسجيل الخطأ والانتقال للموقع التالي
            final_results.append({"المحل": store["name"], "الحالة ⚠️": "الموقع محمي أو غير متاح حالياً"})

    return {
        "تقرير الرادار 🛰️": "فحص شامل للسوق الأردني",
        "النتائج المستخلصة 🎣": final_results
    }
