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
            return "📊 **به‌روزرسانی قیمت‌های روز بازار فولاد**\n\n✅ دریافت اطلاعات از آهن آنلاین با موفقیت انجام شد."
    except Exception as e:
        print(f"Error fetching data: {e}")
    
    return "⚠️ خطا در دریافت اطلاعات از سایت مرجع."

async def main():
    bot = Bot(token=TOKEN)
    message = fetch_steel_prices()
    await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")

if __name__ == "__main__":
    asyncio.run(main())
