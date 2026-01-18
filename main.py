from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import re

app = FastAPI()

# قائمة المواقع المستهدفة 🛒
STORES = [
    {"name": "كارفور الأردن", "url": "https://www.carrefourjordan.com/mafjor/ar/c/NFJOR4000000"},
    {"name": "لولو ماركت", "url": "https://www.luluhypermarket.com/en-jo/pages/instore-promotions"}
]

@app.get("/")
def home():
    return {"message": "الرادار نشط! اذهب إلى /deals لرؤية العروض"}

@app.get("/deals")
def get_deals():
    all_results = []
    # هوية متصفح حقيقية لتجاوز الحماية 🎭
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
        'Referer': 'https://www.google.com/'
    }
    
    # نمط البحث عن الأسعار (مثال: 5.99 JD أو 10 دينار) 💰
    price_pattern = re.compile(r'(\d+\.?\d*)\s*(JD|JOD|دينار)')

    for store in STORES:
        try:
            response = requests.get(store["url"], headers=headers, timeout=20)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # البحث عن أي نص يحتوي على كلمة "دينار" أو "JD"
                for element in soup.find_all(['span', 'p', 'div', 'h3']):
                    text = element.get_text(strip=True)
                    match = price_pattern.search(text)
                    
                    if match and 5 < len(text) < 100:
                        price = match.group(0)
                        # استخراج اسم المنتج عبر حذف السعر من النص
                        name = text.replace(price, "").strip()
                        
                        if name:
                            all_results.append({
                                "المتجر 🏪": store["name"],
                                "المنتج 🍖": name[:50], # نأخذ أول 50 حرف فقط
                                "السعر 💰": price
                            })
        except:
            continue

    # في حال لم يجد الرادار شيئاً، سنعيد رسالة توضيحية بدل القائمة الفارغة
    if not all_results:
        return {"status": "scanning", "message": "المواقع تمنع الوصول حالياً، جاري محاولة تقنيات أخرى..."}
    
    return all_results
