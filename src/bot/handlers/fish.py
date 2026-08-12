import os
import random

from aiogram.types import Message, FSInputFile

from src.data.constants import FISH_DICT
from src.utils.logs import log_decorator


@log_decorator
async def handle_ryba(message: Message):
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