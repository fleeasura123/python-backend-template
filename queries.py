from graphene import List, ObjectType
from graphql_types.user import UserObject
from graphql_types.user_role import UserRoleObject
from graphql_types.permission import PermissionObject


class Query(ObjectType):
    users = List(UserObject)
    roles = List(UserRoleObject)

    async def resolve_users(self, info):
        return []

    async def resolve_roles(self, info):
        return []
