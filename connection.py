from dotenv import dotenv_values
from functools import lru_cache
from psycopg_pool import AsyncConnectionPool


@lru_cache(maxsize=1)
def get_connection_settings():
    config = dotenv_values(".env")
    return f"user={config['DB_USER']} password={config['DB_PASSWORD']} host={config['DB_HOST']} port={config['DB_PORT']} dbname={config['DB_NAME']}"


@lru_cache(maxsize=1)
def get_pool():
    return AsyncConnectionPool(
        conninfo=get_connection_settings(),
        check=AsyncConnectionPool.check_connection,
        max_size=80,
    )
