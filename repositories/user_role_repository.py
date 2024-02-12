from psycopg.rows import class_row
import asyncio

from connection import get_pool
from models.test import Test
from models.user_role import UserRole


class UserRoleRepository:

    async def list(self):
        async with get_pool().connection() as connection:
            async with connection.cursor() as cursor:
                cursor.row_factory = class_row(Test)

                await cursor.execute("SELECT * FROM test WHERE name='test1' FOR UPDATE")

                result = await cursor.fetchone()

                if result is not None:
                    print("Found a row with name test1")

                await asyncio.sleep(5)

                if result is not None:
                    await cursor.execute("INSERT INTO test(name) values('test2')")
                    print("Inserted a row with name test2")

                await cursor.execute("DELETE FROM test WHERE name='test1'")
                print("Deleted a row with name test1")

                return []

    async def list2(self):
        async with get_pool().connection() as connection:
            async with connection.cursor() as cursor:

                await cursor.execute("SELECT * FROM test WHERE name='test1' FOR UPDATE")

                result = await cursor.fetchone()

                if result is not None:
                    print("Found a row with name test1 -- list2")
                else:
                    print("No row with name test1 -- list2")

                return []
