from datetime import datetime
import functools
import logging
from pathlib import Path

from aiogram.types import Message


logger = logging.getLogger("logs")
logger.setLevel(logging.INFO)

logger_messages = logging.getLogger("message_log")
logger_messages.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s -> %(message)s ",
    datefmt="%Y-%m-%d %H:%M:%S"
)

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

BOT_LOG_FILE = LOG_DIR / "bot.log"
MESSAGE_LOG_FILE = LOG_DIR / "bot.log"

file_handler = logging.FileHandler(str(BOT_LOG_FILE), encoding="utf-8")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

file_messages_handler = logging.FileHandler(str(MESSAGE_LOG_FILE), encoding="utf-8")
file_messages_handler.setLevel(logging.INFO)
file_messages_handler.setFormatter(formatter)
logger_messages.addHandler(file_messages_handler)

def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        logger.info(f"Начало выполнения функции {func.__name__}({signature})")

        try:
            start = datetime.now()
            result = func(*args, **kwargs)
            elapsed = (datetime.now() - start).total_seconds()
            logger.info(f"{func.__name__} -> {repr(result)} ({elapsed:.4f}с)")
            return result
        except Exception as e:
            logger.error(f"Ошибка при выполнении функции {func.__name__} | {type(e).__name__}:\n\n {e}")
            raise
    return wrapper

def log_message(message: Message, type_message: str):
    text_message = message.text
    from_username = message.from_user.username
    from_user_id = message.from_user.id
    from_names = f"{message.from_user.first_name} {message.from_user.last_name}"

    logger_messages.info(f"{type_message} | Сообщение от {from_username if from_username is not None else from_names}({from_user_id}) с текстом \"{text_message}\"")