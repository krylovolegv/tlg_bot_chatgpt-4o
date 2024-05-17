import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiohttp import ClientSession, TCPConnector
from app.handlers import router

async def main():
    # Загрузка переменных окружения из файла .env
    load_dotenv()
    # Получаем токен и прокси URL из .env файла
    tg_token = os.getenv('TG_TOKEN')
    proxy_url = os.getenv('PROXY_URL')

    # Создаем сессию с прокси-сервером
    connector = TCPConnector(ssl=False)
    session = ClientSession(connector=connector)
    session.proxy = proxy_url

    # Создаем бота и указываем прокси
    bot = Bot(token=tg_token)

    # Создаем диспетчер и регистрируем роутеры
    dp = Dispatcher()
    dp.include_router(router)

    # Запускаем поллинг
    await dp.start_polling(bot)
    # Закрываем сессию
    await session.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')

