import asyncio
import requests
from bs4 import BeautifulSoup
from telegram import Bot

TOKEN = "8824078270:AAHVz-hAPVmaiM9kuJS9-UP4M1xF6fkDSto"
CHAT_ID = "@foladnamad"

def fetch_steel_prices():
    # تنظیمات پیشرفته برای دور زدن سیستم ضد ربات سایت
    url = "https://ahanonline.com/product-category/میلگرد/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://www.google.com/",
        "Accept-Language": "fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    
    try:
        res = requests.get(url, headers=headers, timeout=20)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            items = []
            # جستجوی مستقیم در سطرها
            rows = soup.find_all('tr')
            
            for row in rows:
                cols = row.find_all('td')
                if len(cols) >= 2:
                    name = cols[0].get_text(strip=True)
                    price = cols[1].get_text(strip=True)
                    if name and price:
                        items.append(f"▫️ {name} | {price}")
            
            if items:
                # فقط ۸ مورد اول را برمی‌داریم که متن خیلی طولانی نشود
                table_text = "\n".join(items[:8])
                return f"📊 **قیمت‌های لحظه‌ای میلگرد (آهن آنلاین)**\n\n{table_text}\n\n📞 استعلام لحظه‌ای با ما در ارتباط باشید."
            
            return "⚠️ سایت پاسخ داد اما جدول قیمت‌ها پیدا نشد. ساختار سایت ممکن است تغییر کرده باشد."
        else:
            return f"⚠️ سایت آهن آنلاین در دسترس نیست (کد وضعیت: {res.status_code})"
            
    except Exception as e:
        return f"⚠️ خطای فنی در اتصال به سایت: {str(e)}"

async def main():
    bot = Bot(token=TOKEN)
    message = fetch_steel_prices()
    await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")

if __name__ == "__main__":
    asyncio.run(main())
