from graphene import Int, ObjectType, String, List, Field

from .user_role import UserRoleObject


class UserObject(ObjectType):
    id = Int()
    first_name = String()
    last_name = String()
    username = String()
    password = String()
    refresh_token = String()
    role_id = Int()
    role = Field(lambda: UserRoleObject)
