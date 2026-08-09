import os
import random

from aiogram import Dispatcher, Bot
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from src.core.config import get_group_id
from src.data.constants import PHRASES, POSTS_PHRASES, FISH_DICT
from src.core.security import get_random_number
from src.bot.ai import handler_private_message

quantity_message: int = 0
fixed_number: int = get_random_number()

class DeveloperStates(StatesGroup):
    waiting_for_message = State()

def register_handlers(dp: Dispatcher, bot: Bot):
    dp.message.register(process_developer_message, StateFilter(DeveloperStates.waiting_for_message))
    dp.message.register(handle_developer_messsage, Command("message_to_developer"))
    dp.message.register(handler_start, CommandStart())
    dp.message.register(handler_ryba, Command("ryba"))
    dp.message.register(handle_message)

async def handler_start(message: Message):
    await message.answer("Я AI рыбка: буль-буль-буль")

async def handler_ryba(message: Message):
    fish_types = FISH_DICT

    random_key = random.choice(list(fish_types.keys()))

    current_dir = os.getcwd()
    photo_path = f"{current_dir}/src/media/photos/{random_key}.jpg"
    if os.path.exists(photo_path):
        photo = FSInputFile(photo_path)
        await message.answer_photo(
            photo=photo,
            caption=f"Ты {fish_types[random_key]}",
            reply_to_message_id=message.message_id
        )

async def handle_developer_messsage(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Напишите своё сообщение Кириллу в следующем сообщении, пожалуйста, буль")
    await state.set_state(DeveloperStates.waiting_for_message)

async def process_developer_message(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Сообщение отправлено!")
    await bot.send_message(chat_id=1982818072, text=message.text)
    await state.clear()

async def handle_message(message: Message, bot: Bot):
    global quantity_message
    global fixed_number

    chat_type = message.chat.type

    if chat_type.lower() == "private":
        print(f"{message.from_user.username} [id={message.from_user.id}] - {message.text}")
        await handler_private_message(message)
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