from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

# الهدف الجديد: صفحة العروض الأردنية في موقع لبيب 🎯
TARGET_URL = "https://www.labeb.com/ar/offers/jordan"

@app.get("/")
def home():
    return {"message": "رادار العروض الأردنية نشط 🛰️"}

@app.get("/deals")
def get_deals():
    all_deals = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(TARGET_URL, headers=headers, timeout=15)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # في موقع لبيب، العروض غالباً ما تكون داخل عناوين h3 🏷️
            items = soup.find_all('h3')
            
            for item in items:
                text = item.get_text(strip=True)
                if len(text) > 3:
                    all_deals.append({
                        "العرض المكتشف 🏷️": text
                    })
            
            return {
                "المصدر 🌐": "لبيب عروض الأردن",
                "عدد العروض المكتشفة 📊": len(all_deals),
                "العروض 🛒": all_deals[:15] # سنعرض أول 15 عرضاً فقط
            }
        else:
            return {"error": f"الموقع لم يستجب بشكل صحيح، كود الحالة: {response.status_code}"}

    except Exception as e:
        return {"error": f"حدث خطأ أثناء الصيد: {str(e)}"}
