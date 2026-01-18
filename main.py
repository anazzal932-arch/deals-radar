from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

# هدف جديد أسهل للاختبار 🎯
TEST_URL = "https://3rodh.com/jordan-offers"

@app.get("/")
def home():
    return {"message": "الرادار نشط! اذهب إلى /deals للاختبار"}

@app.get("/deals")
def get_deals():
    results = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(TEST_URL, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # البحث عن العناوين التي تحتوي على عروض 📰
        titles = soup.find_all(['h2', 'h3'], limit=10)
        
        for item in titles:
            text = item.get_text(strip=True)
            if len(text) > 5:
                results.append({
                    "المتجر/العرض 🏬": text,
                    "الحالة 🔍": "تم اكتشافه بنجاح"
                })
    except Exception as e:
        return {"error": str(e)}

    return results if results else {"message": "حتى هذا الموقع يمنعنا! لنحاول طريقة أخرى."}
