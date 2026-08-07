import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from config import get_bot_token

bot = Bot(token=get_bot_token())
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Я рыбка: буль-буль-буль")

if __name__ == "__main__":
    asyncio.run(main())
