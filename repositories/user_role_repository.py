from psycopg.rows import class_row
import asyncio

from connection import get_pool
from models.user_role import UserRole


class UserRoleRepository:

    async def list(self):
        async with get_pool().connection() as connection:
            async with connection.cursor() as cursor:
                cursor.row_factory = class_row(UserRole)

                await cursor.execute("SELECT * FROM user_roles")

                return await cursor.fetchall()

    async def get_single(self, id):
        async with get_pool().connection() as connection:
            async with connection.cursor() as cursor:
                cursor.row_factory = class_row(UserRole)

                await cursor.execute(
                    "SELECT * FROM user_roles WHERE id = %(id)s", {"id": id}
                )

                return await cursor.fetchone()
