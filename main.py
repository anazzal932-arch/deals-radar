from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from playwright.async_api import async_playwright
import urllib.parse
import httpx  # استخدم httpx بدلاً من requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

async def fetch_image_deals(query: str):
    """الرادار المتطور لصيد صور الكتالوجات 🛰️"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        encoded_query = urllib.parse.quote(f"{query} الأردن 2026")
        url = f"https://www.google.com/search?q={encoded_query}&tbm=isch&tbs=qdr:w"
        
        try:
            await page.goto(url, timeout=60000)
            await page.wait_for_selector("img", timeout=10000)
            
            images = await page.query_selector_all("img")
            links = []
            for img in images:
                src = await img.get_attribute("src")
                if src and src.startswith("http") and len(links) < 5:
                    links.append(src)
            
            await browser.close()
            return links
        except Exception as e:
            print(f"Error fetching image deals: {e}")
            await browser.close()
            return []

async def fetch_social_media_deals(query: str, region: str):
    """جلب العروض من فيسبوك وإنستغرام حسب المنطقة"""
    facebook_deals = await fetch_facebook_deals(query, region)
    instagram_deals = await fetch_instagram_deals(query, region)
    
    return facebook_deals + instagram_deals

async def fetch_facebook_deals(query: str, region: str):
    access_token = 'YOUR_ACCESS_TOKEN'  # استبدل برمز الوصول الخاص بك
    url = f"https://graph.facebook.com/v12.0/search?type=page&q={query}&access_token={access_token}"
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            return data.get('data', [])
        except httpx.HTTPStatusError as e:
            print(f"Error fetching Facebook deals: {e.response.status_code} - {e.response.text}")
            return []
        except Exception as e:
            print(f"Error fetching Facebook deals: {e}")
            return []

async def fetch_instagram_deals(query: str, region: str):
    access_token = 'YOUR_ACCESS_TOKEN'  # استبدل برمز الوصول الخاص بك
    url = f"https://graph.instagram.com/me/media?fields=id,caption&access_token={access_token}"
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            return data.get('data', [])
        except httpx.HTTPStatusError as e:
            print(f"Error fetching Instagram deals: {e.response.status_code} - {e.response.text}")
            return []
        except Exception as e:
            print(f"Error fetching Instagram deals: {e}")
            return []

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "query": "", "deals": []})

@app.get("/best-deal", response_class=HTMLResponse)
async def best_deal(request: Request, query: str = "عروض كارفور", region: str = "الأردن"):
    try:
        # استدعاء صائد العروض من فيسبوك وإنستغرام
        deals = await fetch_social_media_deals(query, region)
        return templates.TemplateResponse("index.html", {
            "request": request,
            "query": query,
            "deals": deals  # نرسل العروض لتعرضها في الواجهة
        })
    except Exception as e:
        print(f"Error in best_deal: {e}")
        raise HTTPException(status_code=500, detail="حدث خطأ داخلي في الخادم.")
