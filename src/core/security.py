import random

from src.utils.logs import log_decorator


@log_decorator
def get_random_number() -> int:
    """Возвращает случайное число от 1 до 30"""
    return random.randint(5, 15)