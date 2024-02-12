from psycopg.rows import class_row

from connection import get_pool
from graphql_types.permission import PermissionObject


class PermissionRepository:

    async def list(self):
        async with get_pool().connection() as connection:
            async with connection.cursor() as cursor:
                cursor.row_factory = class_row(PermissionObject)

                await cursor.execute("SELECT * FROM permissions")

                return await cursor.fetchall()

    async def list_by_role_id(self, role_id: int):
        async with get_pool().connection() as connection:
            async with connection.cursor() as cursor:
                cursor.row_factory = class_row(PermissionObject)
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
