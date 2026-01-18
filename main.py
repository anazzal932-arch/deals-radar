from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

# سنستخدم موقعاً عالمياً بسيطاً جداً لنرى إذا كان الرادار "يصطاد" نصوصاً أصلاً
TEST_STORE = {"name": "موقع اختبار", "url": "https://example.com"}

@app.get("/")
def home():
    return {"message": "رادار العروض نشط 🛰️"}

@app.get("/deals")
def get_deals():
    try:
        # 1. محاولة جلب الموقع
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(TEST_STORE["url"], headers=headers, timeout=10)
        
        # 2. إذا نجح الاتصال
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # لنجلب كل العناوين (h1) والفقرات (p)
            text_data = [t.get_text() for t in soup.find_all(['h1', 'p'])]
            
            return {
                "المحل": TEST_STORE["name"],
                "النصوص التي اصطادها الرادار 🎣": text_data
            }
        else:
            return {"error": f"الموقع رد برمز خطأ: {response.status_code}"}
            
    except Exception as e:
        return {"error": f"تعذر الوصول للموقع: {str(e)}"}
