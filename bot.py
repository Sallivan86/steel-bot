import asyncio
import requests
from bs4 import BeautifulSoup
from telegram import Bot

TOKEN = "8824078270:AAHVz-hAPVmaiM9kuJS9-UP4M1xF6fkDSto"
CHAT_ID = "@foladnamad"

def fetch_steel_prices():
    # استفاده از منبع جایگزین با ساختار HTML مستقیم
    url = "https://www.tgju.org/profile/price_rebar"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        res = requests.get(url, headers=headers, timeout=15)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            # استخراج قیمت‌های اصلی
            items = []
            rows = soup.select('table.market-table tbody tr')
            
            for row in rows:
                cols = row.find_all('td')
                if len(cols) >= 2:
                    title = cols[0].get_text(strip=True)
                    price = cols[1].get_text(strip=True)
                    if title and price:
                        items.append(f"▫️ **{title}**: {price} ریال")
            
            if items:
                table_text = "\n".join(items[:8])
                return f"📊 **قیمت روز مقاطع فولادی - فولاد نماد**\n\n{table_text}\n\n📞 جهت ثبت سفارش و استعلام لحظه‌ای با ما در ارتباط باشید."
            
            # خروجی رزرو در صورت تغییرات لحظه‌ای
            return "📊 **قیمت روز مقاطع فولادی - فولاد نماد**\n\n▫️ میلگرد ۱۴ آجدار | تماس بگیرید\n▫️ میلگرد ۱۶ آجدار | تماس بگیرید\n▫️ تیرآهن ۱۴ | تماس بگیرید\n\n📞 جهت استعلام لحظه‌ای با ما در ارتباط باشید."
            
    except Exception as e:
        print(f"Error: {e}")
    
    return "⚠️ خطا در دریافت اطلاعات از سایت مرجع."

async def main():
    bot = Bot(token=TOKEN)
    message = fetch_steel_prices()
    await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")

if __name__ == "__main__":
    asyncio.run(main())
