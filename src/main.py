import asyncio
import random

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

from config import get_bot_token, get_group_id
from phrases import PHRASES, POSTS_PHRASES
from security import get_random_number

bot = Bot(token=get_bot_token())
dp = Dispatcher()
quantity_message: int = 0
fixed_number: int = get_random_number()

async def main():
    await dp.start_polling(bot)

@dp.message(CommandStart())
async def handler_start(message: Message):
    await message.answer("Я рыбка: буль-буль-буль")

@dp.message()
async def handler_messages(message: Message):
    global quantity_message
    global fixed_number

    chat_type = message.chat.type

    if chat_type.lower() == "private":
        await message.answer("Я дружелюбная рыбка, но тут говорить не могу :)")
        return

    if message.forward_from_chat and message.forward_from_chat.id == get_group_id():
        print(1)
        text: str = random.choice(POSTS_PHRASES)
        await message.answer(
            text,
            reply_to_message_id=message.message_id
        )
        return

    quantity_message += 1
    
    if quantity_message == fixed_number:
        text: str = random.choice(PHRASES)
        await message.answer(
            text,
            reply_to_message_id=message.message_id
        )

        quantity_message = 0
        fixed_number = get_random_number()

if __name__ == "__main__":
    asyncio.run(main())
