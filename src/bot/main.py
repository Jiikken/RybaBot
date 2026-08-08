import asyncio

from aiogram import Bot, Dispatcher

from core.config import get_bot_token
from bot.handlers import register_handlers

bot = Bot(token=get_bot_token())
dp = Dispatcher()

async def main():
    register_handlers(dp=dp)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
