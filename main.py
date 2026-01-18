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
    return {"message": "رادار العروض التلقائي يعمل! استخدم مسار /deals لرؤية النتائج."}

@app.get("/deals")
def get_deals():
    all_results = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # نمط البحث عن السعر (رقم يتبعه JD أو دينار) 💰
    price_pattern = re.compile(r'(\d+\.?\d*)\s*(JD|دينار|JOD)')

    for store in STORES:
        try:
            response = requests.get(store["url"], headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # البحث في العناصر التي عادة ما تحتوي على نصوص المنتجات
            for element in soup.find_all(['div', 'h2', 'h3', 'span']):
                text = element.get_text(strip=True)
                match = price_pattern.search(text)
                
                if match and len(text) < 100:
                    price = match.group(0)
                    # تنظيف النص لاستخراج اسم المنتج (حذف السعر من النص)
                    product_name = text.replace(price, "").strip()
                    
                    if product_name:
                        all_results.append({
                            "المتجر 🏪": store["name"],
                            "المنتج 🍖": product_name,
                            "السعر 💰": price
                        })
        except Exception as e:
            continue

    return all_results[:20] # عرض أول 20 نتيجة منظمة
