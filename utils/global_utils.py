from functools import lru_cache
from dotenv import dotenv_values
import hashlib


@lru_cache(maxsize=1)
def get_config():
    return dotenv_values(".env")


def hash_md5(input_string: str) -> str:
    return hashlib.md5(input_string.encode()).hexdigest()


def generate_random_string():
    import random
    import string

    return "".join(random.choices(string.ascii_letters + string.digits, k=10))
