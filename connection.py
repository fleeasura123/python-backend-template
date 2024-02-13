from functools import lru_cache
from psycopg_pool import AsyncConnectionPool

from utils.global_utils import get_config


@lru_cache(maxsize=1)
def get_connection_settings():
    config = get_config()
    return f"user={config['DB_USER']} password={config['DB_PASSWORD']} host={config['DB_HOST']} port={config['DB_PORT']} dbname={config['DB_NAME']}"


@lru_cache(maxsize=1)
def get_pool():
    return AsyncConnectionPool(
        conninfo=get_connection_settings(),
        max_size=80,
    )
