from psycopg.rows import class_row

from connection import get_pool
from graphql_types.user import UserType


class UserRepository:

    async def get_single(self, id: int) -> UserType:
        async with get_pool().connection() as connection:
            async with connection.cursor() as cursor:
                cursor.row_factory = class_row(UserType)

                await cursor.execute(
                    "SELECT * FROM users WHERE id = %(id)s", {"id": id}
                )

                return await cursor.fetchone()
