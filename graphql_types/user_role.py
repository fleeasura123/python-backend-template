from graphene import Int, ObjectType, String, List, Field

from .permission import PermissionObject
from repositories_instances import *


class UserRoleObject(ObjectType):
    id = Int()
    name = String()
    permissions = Field(List(lambda: PermissionObject), page=Int(default_value=1))

    async def resolve_permissions(root, info, page):
        return permission_repository.list_by_role(root.id, page)
