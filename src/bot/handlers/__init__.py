from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command, StateFilter

from src.bot.handlers.developer import DeveloperStates, handle_developer_messsage, process_developer_message
from src.bot.handlers.fish import handle_ryba
from src.bot.handlers.group import handle_message
from src.bot.handlers.send_messages import handle_send_message
from src.bot.handlers.start import handle_start 


def register_handlers(dp: Dispatcher, bot: Bot):
    dp.message.register(process_developer_message, StateFilter(DeveloperStates.waiting_for_message))
    dp.message.register(handle_developer_messsage, Command("feedback"))
    dp.message.register(handle_send_message, Command("love"))
    dp.message.register(handle_start, CommandStart())
    dp.message.register(handle_ryba, Command("ryba"))
    dp.message.register(handle_message)