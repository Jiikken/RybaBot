import os
import asyncio
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession

from src.core.config import get_bot_token
from src.bot.handlers import register_handlers
from src.utils.logs import log_decorator

load_dotenv()


session = AiohttpSession(proxy=os.getenv("PROXY_URL"))
bot = Bot(token=get_bot_token(), session=session)
dp = Dispatcher()

@log_decorator
async def main():
    register_handlers(dp=dp, bot=bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
