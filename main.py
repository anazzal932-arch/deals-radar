def google_rss_search(query: str):
    # ترميز البحث للغة العربية 🛠️
    encoded_query = urllib.parse.quote(f"{query} عروض الأردن")
    url = f"https://news.google.com/rss/search?q={encoded_query}&hl=ar&gl=JO&ceid=JO:ar"
    
    feed = feedparser.parse(url)
    deals = []

    for entry in feed.entries:
        full_text = entry.title + " " + entry.get("summary", "")
        
        # 1. تطوير الصنارة: البحث عن الأرقام العربية (١٥٠) والإنجليزية (150) 🎣
        # أضفنا \u0660-\u0669 للتعرف على الأرقام الهندية المستخدمة في العربية
        price_match = re.search(r"([\d\u0660-\u0669]+(\.[\d\u0660-\u0669]+)?)\s?(دينار|JD|JOD|د\.أ)", full_text)
        
        # تحويل السعر المكتشف إلى رقم حقيقي (Float) للترتيب 💸
        price = None
        if price_match:
            price_str = price_match.group(1)
            # كود بسيط لتحويل الأرقام العربية إلى إنجليزية إذا وجدت
            arabic_digits = "٠١٢٣٤٥٦٧٨٩"
            english_digits = "0123456789"
            translation_table = str.maketrans(arabic_digits, english_digits)
            price = float(price_str.translate(translation_table))

        # 2. تنظيف العنوان: حذف اسم الموقع من العنوان 🏛️
        clean_title = entry.title.split(" - ")[0]

        deals.append({
            "المنتج 🛒": clean_title,
            "السعر المستخرج 💸": price if price else "يحدد لاحقاً",
            "المصدر 🏛️": entry.source.title if hasattr(entry, 'source') else "جوجل",
            "الرابط 🔗": entry.link
        })
    
    # 3. ترتيب النتائج: الأرخص أولاً (إذا وُجد السعر) 📉
    return sorted(deals, key=lambda x: (x["السعر المستخرج 💸"] is None, x["السعر المستخرج 💸"]))
