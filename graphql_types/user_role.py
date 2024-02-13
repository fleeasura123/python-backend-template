from graphene import Int, ObjectType, String, List, Field

from .permission import PermissionType
from repositories.permission_repository import PermissionRepository

# Repositories instances
permission_repository = PermissionRepository()


class UserRoleType(ObjectType):
    id = Int()
    name = String()
    permissions = List(lambda: PermissionType)

    async def resolve_permissions(self, info):
        return await permission_repository.get_by_role_id(self.id)
