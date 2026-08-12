from os import getenv
from dotenv import load_dotenv

from src.utils.logs import log_decorator


load_dotenv()

@log_decorator
def get_bot_token():
    return getenv("TEST_BOT_TOKEN")

@log_decorator
def get_group_id():
    return getenv("GROUP_ID")