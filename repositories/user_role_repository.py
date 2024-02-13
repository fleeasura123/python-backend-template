from graphql import GraphQLError
from psycopg.rows import class_row

from connection import get_pool
from graphql_types.user_role import UserRoleType


class UserRoleRepository:

    async def get(self) -> list[UserRoleType]:
        async with get_pool().connection() as connection:
            async with connection.cursor() as cursor:
                cursor.row_factory = class_row(UserRoleType)

                await cursor.execute("SELECT * FROM user_roles")

                return await cursor.fetchall()

    async def get_single(self, id: int) -> UserRoleType:
        async with get_pool().connection() as connection:
            async with connection.cursor() as cursor:
                cursor.row_factory = class_row(UserRoleType)

                await cursor.execute(
                    "SELECT * FROM user_roles WHERE id = %(id)s", {"id": id}
                )

                user_role = await cursor.fetchone()

                if user_role is None:
                    raise GraphQLError("User role not found")

                return user_role
