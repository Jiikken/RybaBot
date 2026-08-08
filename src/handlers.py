import os
import random

from aiogram import Dispatcher
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart, Command

from config import get_group_id
from constants import PHRASES, POSTS_PHRASES, FISH_DICT
from security import get_random_number

quantity_message: int = 0
fixed_number: int = get_random_number()

def register_handlers(dp: Dispatcher):
    dp.message.register(handler_start, CommandStart())
    dp.message.register(handler_ryba, Command("ryba"))
    dp.message.register(handler_messages)

async def handler_start(message: Message):
    await message.answer("Я рыбка: буль-буль-буль")

async def handler_ryba(message: Message):
    fish_types = FISH_DICT

    random_key = random.choice(list(fish_types.keys()))

    current_dir = os.getcwd()
    photo_path = f"{current_dir}/src/photos/{random_key}.jpg"
    if os.path.exists(photo_path):
        photo = FSInputFile(photo_path)
        await message.answer_photo(
            photo=photo,
            caption=f"Ты {fish_types[random_key]}",
            reply_to_message_id=message.message_id
        )

async def handler_messages(message: Message):
    global quantity_message
    global fixed_number

    chat_type = message.chat.type

    if chat_type.lower() == "private":
        await message.answer("Я дружелюбная рыбка, но тут говорить не могу :)")
        return

    if message.forward_from_chat and message.forward_from_chat.id == int(get_group_id()):
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