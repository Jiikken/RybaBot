import asyncio
import random

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from config import get_bot_token
from phrases import PHRASES
from security import get_random_number

bot = Bot(token=get_bot_token())
dp = Dispatcher()
quantity_message: int = 0
fixed_number: int = get_random_number()

async def main():
    await dp.start_polling(bot)

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Я рыбка: буль-буль-буль")

@dp.message()
async def handler_messages(message: Message):
    global quantity_message
    quantity_message += 1
    print(f"quantity_message={quantity_message}")
    print(f"fixed_number={fixed_number}")
    if quantity_message == fixed_number:
        text: str = random.choice(PHRASES)
        await message.answer(text)
        quantity_message = 0
        fixed_number = get_random_number()

if __name__ == "__main__":
    asyncio.run(main())
