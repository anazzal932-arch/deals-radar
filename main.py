from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from playwright.async_api import async_playwright
import asyncio

app = FastAPI()

# إعداد المجلد الذي يحتوي على صفحات HTML
templates = Jinja2Templates(directory="templates")

async def fetch_carrefour_deals():
    """هذه الدالة هي 'الرادار' الذي يبحث في جوجل ويصطاد الصور"""
    async with async_playwright() as p:
        # تشغيل متصفح خفي (لا يراه المستخدم)
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # البحث عن عروض كارفور الأردن 2026 مع فلتر 'آخر أسبوع' باستخدام tbs=qdr:w
        search_query = "عروض كارفور الأردن 2026"
        url = f"https://www.google.com/search?q={search_query}&tbm=isch&tbs=qdr:w"
        
        await page.goto(url)
        
        # الانتظار حتى تظهر الصور في الصفحة
        await page.wait_for_selector("img")
        
        # استخراج روابط أول 5 صور
        images = await page.query_selector_all("img")
        image_urls = []
        
        for img in images:
            src = await img.get_attribute("src")
            # نتأكد أن الرابط يبدأ بـ http لضمان أنه رابط صورة حقيقي
            if src and src.startswith("http") and len(image_urls) < 5:
                image_urls.append(src)
        
        await browser.close()
        return image_urls

@app.get("/")
async def read_root(request: Request):
    """هذه الدالة تعمل عند فتح الموقع وترسل الصور للقالب"""
    try:
        # استدعاء الرادار لجلب الصور
        deals_images = await fetch_carrefour_deals()
    except Exception as e:
        print(f"حدث خطأ أثناء البحث: {e}")
        deals_images = [] # في حال حدث خطأ نرسل قائمة فارغة

    return templates.TemplateResponse("index.html", {
        "request": request, 
        "deals": deals_images
    })
