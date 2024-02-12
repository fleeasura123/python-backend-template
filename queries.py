from graphene import List, ObjectType

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
    roles2 = List(UserRoleObject)
    permissions = List(PermissionObject)

    async def resolve_users(self, info):
        return []

    async def resolve_roles(self, info):
        return await user_role_repository.list()

    async def resolve_roles2(self, info):
        return await user_role_repository.list2()

    async def resolve_permissions(self, info):
        return await PermissionRepository().list()
