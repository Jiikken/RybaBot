from aiogram.types import Message


async def handle_start(message: Message):
    await message.answer("Я AI рыбка: буль-буль-буль")