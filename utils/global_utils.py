from functools import lru_cache
from dotenv import dotenv_values


@lru_cache(maxsize=1)
def get_config():
    return dotenv_values(".env")
