from aiogram import Bot
from aiogram.types import Message
from src.utils.logs import log_decorator


@log_decorator
async def handle_send_message(message: Message, bot: Bot):
    await message.answer("Сообщение <b>отправлено!</b>",
                         parse_mode="HTML")
    
    await bot.send_message(
        chat_id=6290423468,
        text=f"<blockquote>Люблю тебя очень сильно</blockquote>\n\n" +
            f"От {message.from_user.first_name} ({message.from_user.id})",
        parse_mode="HTML"
        )