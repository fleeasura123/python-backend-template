from graphene import Int, ObjectType, String, List, Field

from .permission import PermissionObject
from repositories.permission_repository import PermissionRepository

# Repositories instances
permission_repository = PermissionRepository()


class UserRoleObject(ObjectType):
    id = Int()
    name = String()
    permissions = List(lambda: PermissionObject)

    async def resolve_permissions(self, info):
        return await permission_repository.list_by_role_id(self.id)
