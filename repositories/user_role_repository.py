from graphql import GraphQLError
from psycopg.rows import class_row

from connection import get_pool
from graphql_types.user_role import UserRoleObject


class UserRoleRepository:

    async def list(self):
        async with get_pool().connection() as connection:
            async with connection.cursor() as cursor:
                cursor.row_factory = class_row(UserRoleObject)

                await cursor.execute("SELECT * FROM user_roles")

                return await cursor.fetchall()

    async def get_single(self, id: int):
        async with get_pool().connection() as connection:
            async with connection.cursor() as cursor:
                cursor.row_factory = class_row(UserRoleObject)

                await cursor.execute(
                    "SELECT * FROM user_roles WHERE id = %(id)s", {"id": id}
                )

                user_role = await cursor.fetchone()

                if user_role is None:
                    raise GraphQLError("User role not found")

                return user_role
