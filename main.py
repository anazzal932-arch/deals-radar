from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import re

app = FastAPI()

# قائمة المواقع المستهدفة في الأردن 🇯🇴
STORES = [
    {"name": "كارفور الأردن", "url": "https://www.carrefourjordan.com/mafjor/ar/c/NFJOR4000000"},
    {"name": "لولو هايبر ماركت", "url": "https://www.luluhypermarket.com/en-jo/pages/instore-promotions"}
]

@app.get("/")
def home():
    return {"message": "رادار العروض المطور يعمل! استخدم مسار /deals"}

@app.get("/deals")
def get_deals():
    all_results = []
    # تحديث الـ Headers للتنكر كمتصفح حقيقي 🎭
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'Accept-Language': 'ar,en;q=0.9',
        'Referer': 'https://www.google.com/'
    }
    
    # نمط البحث عن السعر (رقم يتبعه JD أو دينار) 💰
    price_pattern = re.compile(r'(\d+\.?\d*)\s*(JD|دينار|JOD)')

    for store in STORES:
        try:
            # إضافة سطر للتحقق من الاتصال
            response = requests.get(store["url"], headers=headers, timeout=15)
            if response.status_code != 200:
                continue
                
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # محاولة البحث في نصوص أوسع لاستخراج البيانات
            elements = soup.find_all(['div', 'h2', 'h3', 'span', 'p'])
            
            for element in elements:
                text = element.get_text(strip=True)
                match = price_pattern.search(text)
                
                # شرط إضافي لضمان جودة النتائج (طول النص بين 5 و 80 حرفاً)
                if match and 5 < len(text) < 80:
                    price = match.group(0)
                    product_name = text.replace(price, "").replace("JOD", "").replace("JD", "").strip()
                    
                    if len(product_name) > 2:
                        all_results.append({
                            "المتجر 🏪": store["name"],
                            "المنتج 🍖": product_name,
                            "السعر 💰": price
                        })
        except Exception as e:
            print(f"Error scanning {store['name']}: {e}")
            continue

    # إزالة التكرار في النتائج
    unique_results = [dict(t) for t in {tuple(d.items()) for d in all_results}]
    return unique_results[:30]
