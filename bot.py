import asyncio

from config import TOKEN

from aiogram import Bot, Dispatcher
from handlers import router
from database import create_table

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(router)

async def main():

    create_table()
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")