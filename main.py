from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from playwright.async_api import async_playwright
import asyncio

app = FastAPI()
templates = Jinja2Templates(directory="templates")

async def fetch_carrefour_deals():
    """الرادار الذي يبحث في جوجل كروم عن أحدث العروض"""
    async with async_playwright() as p:
        # تشغيل المتصفح (Chromium هو المحرك المشغل لكروم)
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # البحث عن عروض كارفور الأردن 2026 
        # tbs=qdr:w تضمن أن الصور من 'آخر أسبوع' فقط
        url = "https://www.google.com/search?q=عروض+كارفور+الأردن+2026&tbm=isch&tbs=qdr:w"
        
        try:
            await page.goto(url, timeout=60000)
            await page.wait_for_selector("img", timeout=10000)
            
            # استخراج روابط الصور
            images = await page.query_selector_all("img")
            image_urls = []
            
            for img in images:
                src = await img.get_attribute("src")
                # نتجنب الصور الصغيرة جداً (Base64) ونأخذ الروابط الحقيقية
                if src and src.startswith("http") and len(image_urls) < 5:
                    image_urls.append(src)
            
            await browser.close()
            return image_urls
        except Exception as e:
            print(f"Error: {e}")
            await browser.close()
            return []

@app.get("/")
async def read_root(request: Request):
    # تشغيل الرادار لجلب أحدث 5 صفحات
    deals_images = await fetch_carrefour_deals()
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "deals": deals_images
    })
