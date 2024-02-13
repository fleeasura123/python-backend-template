from psycopg.rows import class_row

from connection import get_pool
from graphql_types.user import UserType
from utils.global_utils import generate_random_string, hash_md5


class UserRepository:

    async def get_single(self, id: int) -> UserType:
        async with get_pool().connection() as connection:
            async with connection.cursor() as cursor:
                cursor.row_factory = class_row(UserType)

                await cursor.execute(
                    "SELECT * FROM users WHERE id = %(id)s", {"id": id}
                )

                return await cursor.fetchone()

    async def change_password(
        self, id: int, old_password: str, new_password: str
    ) -> bool:
        async with get_pool().connection() as connection:
            async with connection.cursor() as cursor:
                cursor.row_factory = class_row(UserType)

                await cursor.execute(
                    "SELECT * FROM users WHERE id = %(id)s LIMIT 1 FOR UPDATE",
                    {"id": id},
                )

                user = await cursor.fetchone()

                if user:

                    if user.password != hash_md5(old_password + user.salt):
                        raise Exception("Incorrect old password")

                    salt = generate_random_string()
                    new_password = hash_md5(new_password + salt)

                    await cursor.execute(
                        "UPDATE users SET password = %(new_password)s, salt=%(salt)s WHERE id = %(id)s",
                        {"id": id, "new_password": new_password, "salt": salt},
                    )

                    return True
                else:
                    raise Exception("User not found")
