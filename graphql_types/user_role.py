from graphene import Int, ObjectType, String, List, Field

from .permission import PermissionObject


class UserRoleObject(ObjectType):
    id = Int()
    name = String()
    permissions = Field(List(lambda: PermissionObject))
