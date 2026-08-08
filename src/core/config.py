from os import getenv
from dotenv import load_dotenv

load_dotenv()

def get_bot_token():
    return getenv("BOT_TOKEN")

def get_group_id():
    return getenv("GROUP_ID")