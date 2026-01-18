from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

# هدف جديد وأكثر انفتاحاً 🎯
TARGET_URL = "https://www.extra-jordan.com/ar/offers"

@app.get("/")
def home():
    return {"message": "رادار عروض إكسترا الأردن يعمل 🛰️"}

@app.get("/deals")
def get_deals():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(TARGET_URL, headers=headers, timeout=15)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # الرادار سيبحث عن أي نصوص داخل عناوين العروض h2 و h3
            found_items = []
            for item in soup.find_all(['h2', 'h3']):
                text = item.get_text(strip=True)
                if len(text) > 5:
                    found_items.append({"العرض المكتشف 🏷️": text})

            if not found_items:
                return {"message": "الرادار دخل للموقع لكن العروض تظهر كصور فقط حالياً 🖼️"}

            return {
                "المحل": "Extra Jordan",
                "قائمة العروض 📉": found_items
            }
        else:
            return {"error": f"الموقع رد بكود: {response.status_code}. سنحاول البحث عن رابط بديل."}

    except Exception as e:
        return {"error": f"خطأ في الاتصال: {str(e)}"}
