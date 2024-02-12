from graphene import Field, Int, List, ObjectType, String

from graphql_types.user import UserObject
from graphql_types.user_role import UserRoleObject
from graphql_types.permission import PermissionObject
from repositories.user_role_repository import UserRoleRepository
from repositories.permission_repository import PermissionRepository

# Repositories instances
user_role_repository = UserRoleRepository()


class Query(ObjectType):
    users = List(UserObject)
    roles = List(UserRoleObject)
    role = Field(UserRoleObject, id=Int(required=True))
    permissions = List(PermissionObject)

    async def resolve_users(self, info):
        return []

    async def resolve_roles(self, info):
        return await user_role_repository.list()

    async def resolve_permissions(self, info):
        return await PermissionRepository().list()

    async def resolve_role(self, info, id):
        return await user_role_repository.get_single(id)
