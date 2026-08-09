from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class DeveloperStates(StatesGroup):
    waiting_for_message = State()

async def handle_developer_messsage(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Напишите своё сообщение <b>Кириллу</b> в следующем сообщении, буль ✍🏻",
                         parse_mode="HTML")
    await state.set_state(DeveloperStates.waiting_for_message)

async def process_developer_message(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Сообщение <b>отправлено!</b>💬",
                         parse_mode="HTML")
    
    await bot.send_message(
        chat_id=1982818072,
        text=f"<blockquote>{message.text}</blockquote>\n\n" +
            f"От {message.from_user.first_name} ({message.from_user.id})",
        parse_mode="HTML"
        )
    
    await state.clear()