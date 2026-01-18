from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from playwright.async_api import async_playwright
import urllib.parse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

async def fetch_image_deals(query: str, region: str = "الأردن"):
    """الرادار الذي يصطاد الصور من الإنترنت 🕸️"""
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            
            # صياغة البحث لجلب أحدث الصور خلال أسبوع
            encoded_query = urllib.parse.quote(f"{query} {region} 2026")
            url = f"https://www.google.com/search?q={encoded_query}&tbm=isch&tbs=qdr:w"
            
            await page.goto(url, timeout=60000)
            await page.wait_for_selector("img", timeout=10000)
            
            images = await page.query_selector_all("img")
            deals = []
            for img in images:
                src = await img.get_attribute("src")
                if src and src.startswith("http") and len(deals) < 10:
                    deals.append({
                        "image_url": src,
                        "description": await img.get_attribute("alt")
                    })
            
            await browser.close()
            return deals
        except Exception as e:
            print(f"خطأ في الرادار: {e}")
            print(f"Traceback: {e.__traceback__}")
            return []

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "query": "", "region": "", "deals": []})

@app.get("/best-deal", response_class=HTMLResponse)
async def best_deal(request: Request, query: str = "عروض", region: str = "الأردن"):
    try:
        # تفعيل الرادار 🔍
        deals = await fetch_image_deals(query, region)
        return templates.TemplateResponse("index.html", {
            "request": request,
            "query": query,
            "region": region,
            "deals": deals
        })
    except Exception as e:
        print(f"خطأ في best_deal: {e}")
        print(f"Traceback: {e.__traceback__}")
        raise HTTPException(status_code=500, detail="حدث خطأ داخلي في الخادم.")
