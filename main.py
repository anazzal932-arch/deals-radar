from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

# الرابط المستهدف: صفحة عروض الأردن في لبيب 🎯
TARGET_URL = "https://www.labeb.com/ar/offers/jordan"

@app.get("/")
def home():
    return {"status": "online", "message": "رادار لبيب جاهز للصيد 🛰️"}

@app.get("/deals")
def get_deals():
    all_deals = []
    
    # هوية متصفح قوية لتجاوز الحظر 🕵️‍♂️
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'ar,en-US;q=0.9',
        'Referer': 'https://www.google.com/'
    }

    try:
        # إرسال الطلب للموقع
        response = requests.get(TARGET_URL, headers=headers, timeout=20)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # في موقع لبيب، العروض غالباً ما تكون داخل عناوين h3 🏷️
            # سنحاول جمع النصوص من العناوين والفقرات
            items = soup.find_all(['h3', 'h2'])
            
            for item in items:
                text = item.get_text(strip=True)
                # تصفية النصوص القصيرة جداً لضمان جودة البيانات
                if len(text) > 10: 
                    all_deals.append({
                        "العرض 🛒": text
                    })
            
            if not all_deals:
                return {"message": "الرادار وصل للموقع لكن لم يجد نصوصاً، قد يكون الموقع محمياً بـ JavaScript 🧱"}
                
            return {
                "المصدر 🌐": "لبيب - Jordan Offers",
                "النتائج 📊": all_deals[:20]
            }
        else:
            return {"error": f"الموقع رفض الدخول، كود الحالة: {response.status_code}"}

    except Exception as e:
        return {"error": f"تعذر الاتصال بالموقع: {str(e)}"}
