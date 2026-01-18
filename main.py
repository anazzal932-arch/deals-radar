from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "رادار العروض يعمل بنجاح!"}

@app.get("/scan")
def scan_url(url: str):
    try:
        # 1. الدخول إلى الموقع
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'lxml')
        
        offers = []
        
        # 2. البحث عن "الحاويات" التي قد تحتوي على عروض
        # نبحث عن النصوص التي تحتوي على أرقام متبوعة بـ % أو كلمة خصم أو ج.د (دينار)
        pattern = re.compile(r'(\d+%)|خصم|تنزيلات|عرض|دينار')
        
        for element in soup.find_all(['div', 'span', 'p', 'h2', 'h3']):
            text = element.get_text(strip=True)
            if pattern.search(text) and len(text) < 100: # لضمان أخذ العناوين وليس فقرات طويلة
                offers.append(text)
        
        # تنظيف النتائج المكررة
        unique_offers = list(set(offers))
        
        return {
            "source": url,
            "status": "success",
            "found_offers": unique_offers[:10] # نأخذ أول 10 عروض تم اكتشافها
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
