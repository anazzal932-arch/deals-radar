from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import re

app = FastAPI()

# سنستخدم هذا الرابط كمختبر للتأكد من أن الرادار "يصطاد" بنجاح 🎣
TEST_STORE = {
    "name": "عروض الأردن (عقرباوي مول وغيره)", 
    "url": "https://3rodh.com/jordan-offers"
}

@app.get("/")
def home():
    return {"message": "الرادار جاهز للاختبار! اذهب إلى /deals"}

@app.get("/deals")
def get_deals():
    all_results = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(TEST_STORE["url"], headers=headers, timeout=15)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # البحث عن نصوص العروض والأسعار 🏷️
        for element in soup.find_all(['h2', 'h3', 'p', 'span']):
            text = element.get_text(strip=True)
            # إذا وجدنا كلمة "عرض" أو "دينار" أو "JD"
            if any(key in text for key in ["عرض", "دينار", "JD", "JOD"]):
                all_results.append({
                    "المصدر 🏪": TEST_STORE["name"],
                    "التفاصيل 📄": text[:80]
                })
    except Exception as e:
        return {"error": f"مشكلة في الاتصال: {str(e)}"}

    return all_results if all_results else {"status": "empty", "message": "لم يتم العثور على نصوص تطابق البحث"}
