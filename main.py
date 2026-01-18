from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

# سنبقي على الموقع الحالي للاختبار 🎯
TEST_STORE = {"name": "عقرباوي مول / عروض الأردن", "url": "https://3rodh.com/jordan-offers"}

@app.get("/")
def home():
    return {"message": "رادار الاختبار يعمل! جرب مسار /deals"}

@app.get("/deals")
def get_deals():
    all_text = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(TEST_STORE["url"], headers=headers, timeout=15)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # الرادار سيلتقط الآن أي نص داخل الروابط والعناوين 🔍
            elements = soup.find_all(['a', 'h2', 'h3'])
            
            for el in elements:
                text = el.get_text(strip=True)
                if len(text) > 2: # نتأكد أن النص ليس فارغاً
                    all_text.append(text)
            
            return {
                "المحل": TEST_STORE["name"],
                "النصوص المكتشفة 🎣": all_text[:20] # سنعرض أول 20 نص فقط للسرعة
            }
        else:
            return {"error": f"الموقع لم يستجب، كود الحالة: {response.status_code}"}

    except Exception as e:
        return {"error": str(e)}
