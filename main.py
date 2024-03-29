import asyncio
import aiohttp
import random
from bs4 import BeautifulSoup
from telegram import Bot
from datetime import datetime

TELEGRAM_BOT_TOKEN = '6254161040:AAHihmIfvjK03TlOvk7-Y3UrgQo5RIvow4Q'
TELEGRAM_CHAT_ID = '280019658'
URL = 'https://starkpepe.xyz/'

bot = Bot(token=TELEGRAM_BOT_TOKEN)

async def fetch_page(session, url):
    try:
        async with session.get(url) as response:
            return await response.text()
    except Exception as e:
        print(f"Ошибка при запросе: {e}")
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=f"Ошибка при запросе: {e}")


async def check_element(session):
    html = await fetch_page(session, URL)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        element = soup.find('div', {'class': 'text-neutral-600 cursor-not-allowed h-7'})
        if element is None or element.text != 'NFTs':
            await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="Пора фармить нфт! Элемент не найден или текст отличается!")
            print("Пора фармить нфт! Элемент не найден или текст отличается!")
        else:
            current_time = datetime.now().time()
            print("Ок. Текущее время:", current_time)

async def main():
    async with aiohttp.ClientSession() as session:
        while True:
            await check_element(session)
            await asyncio.sleep(random.randint(5, 7))

if __name__ == '__main__':
    asyncio.run(main())

