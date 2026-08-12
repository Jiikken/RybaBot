import random

from aiogram import Bot
from aiogram.types import Message

from src.core.config import get_group_id
from src.data.constants import PHRASES, POSTS_PHRASES
from src.core.security import get_random_number
from src.bot.ai import handler_private_message
from src.utils.logs import log_decorator


quantity_message: int = 0
fixed_number: int = get_random_number()

@log_decorator
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