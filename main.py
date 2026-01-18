from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import re

app = FastAPI()

# سنركز الاختبار الآن على عقرباوي مول 🛒
TEST_STORE = {"name": "عقرباوي مول", "url": "https://www.facebook.com/AqrabawiMall/"}

@app.get("/deals")
def test_deals():
    all_results = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(TEST_STORE["url"], headers=headers, timeout=15)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # لنحاول استخراج أي نص يحتوي على أرقام أو كلمات متعلقة بالأسعار
        for element in soup.find_all(['span', 'p', 'div']):
            text = element.get_text(strip=True)
            if any(key in text for key in ["دينار", "JD", "JOD", "سعر"]):
                all_results.append({
                    "المحل": TEST_STORE["name"],
                    "النص الملتقط": text[:100]
                })
    except Exception as e:
        return {"error": str(e)}

    return all_results if all_results else {"message": "الرادار لم يجد نصوصاً واضحة، قد تحتاج الصفحة لتقنية محاكاة المتصفح"}
