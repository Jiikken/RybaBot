from aiogram.types import Message
from src.utils.logs import log_decorator


@log_decorator
async def handle_start(message: Message):
    await message.answer("Я AI рыбка: буль-буль-буль")