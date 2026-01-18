from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from playwright.async_api import async_playwright
import urllib.parse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

async def fetch_image_deals(query: str):
    """الرادار الذي يغوص في الإنترنت لصيد الصور 🕸️"""
    async with async_playwright() as p:
        # تشغيل المتصفح بوضعية الخفاء
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # صياغة رابط البحث عن الصور (أحدث النتائج خلال أسبوع)
        encoded_query = urllib.parse.quote(f"{query} عروض الأردن 2026")
        url = f"https://www.google.com/search?q={encoded_query}&tbm=isch&tbs=qdr:w"
        
        try:
            await page.goto(url, timeout=60000)
            await page.wait_for_selector("img", timeout=10000)
            
            # جمع روابط أول 5 صور حقيقية
            images = await page.query_selector_all("img")
            links = []
            for img in images:
                src = await img.get_attribute("src")
                if src and src.startswith("http") and len(links) < 5:
                    links.append(src)
            
            await browser.close()
            return links
        except Exception as e:
            print(f"خطأ أثناء الصيد: {e}")
            await browser.close()
            return []

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """الصفحة الرئيسية للموقع"""
    return templates.TemplateResponse("index.html", {"request": request, "query": "", "deals": []})

@app.get("/best-deal", response_class=HTMLResponse)
async def best_deal(request: Request, query: str = "عروض كارفور"):
    """المسار الذي يعالج عملية البحث ويعرض الصور"""
    # استدعاء رادار الصور بناءً على كلمة البحث 🕵️‍♂️
    images = await fetch_image_deals(query)
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "query": query,
        "deals": images
    })
