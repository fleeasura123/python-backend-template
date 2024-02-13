from psycopg.rows import class_row

from connection import get_pool
from graphql_types.permission import PermissionType


class PermissionRepository:

    async def get(self) -> list[PermissionType]:
        async with get_pool().connection() as connection:
            async with connection.cursor() as cursor:
                cursor.row_factory = class_row(PermissionType)

                await cursor.execute("SELECT * FROM permissions")

                return await cursor.fetchall()

    async def get_by_role_id(self, role_id: int) -> list[PermissionType]:
        async with get_pool().connection() as connection:
            async with connection.cursor() as cursor:
                cursor.row_factory = class_row(PermissionType)

                await cursor.execute(
                    """
                        SELECT
                            permissions.id as id,
                            permissions.name as name
                        FROM
                            permissions
                        INNER JOIN user_roles_permissions ON user_roles_permissions.permission_id = permissions.id
                        WHERE
                            user_roles_permissions.user_role_id = %(role_id)s
                        
                    """,
                    {"role_id": role_id},
                )

                return await cursor.fetchall()
