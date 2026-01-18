from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

# الرابط المحدث (الأكثر استقراراً) 🎯
TARGET_URL = "https://www.labeb.com/ar/offers"

@app.get("/")
def home():
    return {"message": "رادار العروض الأردنية المطور يعمل 🛰️"}

@app.get("/deals")
def get_deals():
    all_deals = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(TARGET_URL, headers=headers, timeout=15)
        
        # إذا واجهنا 404 أو أي خطأ، سنعرف فوراً
        if response.status_code != 200:
            return {"error": f"الموقع غير متاح حالياً، كود الحالة: {response.status_code}"}

        soup = BeautifulSoup(response.content, 'html.parser')
        
        # سنبحث عن أي نص يحتوي على كلمة "دينار" أو "JD" لضمان اصطياد الأسعار 💰
        # نبحث في العناوين والفقرات
        for element in soup.find_all(['h3', 'p', 'span']):
            text = element.get_text(strip=True)
            if any(keyword in text for keyword in ["دينار", "JD", "عرض", "%"]):
                if len(text) > 5:
                    all_deals.append({"العرض 🛒": text})

        return {
            "المصدر 🌐": "لبيب عروض",
            "عدد الصيد 🎣": len(all_deals),
            "القائمة": all_deals[:15]
        }

    except Exception as e:
        return {"error": f"حدث خطأ تقني: {str(e)}"}
