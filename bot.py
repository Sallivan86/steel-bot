import asyncio
import requests
from bs4 import BeautifulSoup
from telegram import Bot

TOKEN = "8824078270:AAHVz-hAPVmaiM9kuJS9-UP4M1xF6fkDSto"
CHAT_ID = "@foladnamad"

def fetch_steel_prices():
    url = "https://ahanonline.com/product-category/%d9%85%db%8c%d9%84%da%af%d8%b1%d8%af/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    try:
        res = requests.get(url, headers=headers, timeout=15)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            items = []
            rows = soup.find_all('tr', limit=8)
            for row in rows:
                cols = row.find_all(['td', 'th'])
                text_cols = [c.get_text(strip=True) for c in cols if c.get_text(strip=True)]
                if len(text_cols) >= 3:
                    items.append(f"🔹 {' | '.join(text_cols[:3])}")
            if items:
                table_text = "\n".join(items[:6])
                return f"📊 **جدول قیمت روز میلگرد - فولاد نماد**\n\n{table_text}\n\n📞 جهت ثبت سفارش و استعلام لحظه‌ای با ما در ارتباط باشید."
            return "📊 **به‌روزرسانی قیمت‌های روز بازار فولاد**\nاطلاعات جدید در حال بارگذاری است."
    except Exception as e:
        print(f"Error: {e}")
    return "⚠️ خطا در دریافت اطلاعات."

async def main():
    bot = Bot(token=TOKEN)
    message = fetch_steel_prices()
    await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")

if __name__ == "__main__":
    asyncio.run(main())
