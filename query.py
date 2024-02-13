from graphene import Field, Int, List, ObjectType, String

from graphql_types.user import UserType
from graphql_types.user_role import UserRoleType
from graphql_types.permission import PermissionType
from repositories.user_role_repository import UserRoleRepository
from repositories.permission_repository import PermissionRepository
from custom_decorators.authorize import authorize

# Repositories instances
user_role_repository = UserRoleRepository()


class Query(ObjectType):
    users = List(UserType)
    roles = List(UserRoleType)
    role = Field(UserRoleType, id=Int(required=True))
    permissions = List(PermissionType)

    async def resolve_users(self, info):
        return []

    @authorize()
    async def resolve_roles(self, info):
        return await user_role_repository.get()

    @authorize()
    async def resolve_permissions(self, info):
        return await PermissionRepository().get()

    @authorize()
    async def resolve_role(self, info, id):
        return await user_role_repository.get_single(id)
