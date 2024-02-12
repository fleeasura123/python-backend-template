from graphene import Boolean, Int, ObjectType, String, Field

from .user_role import UserRoleObject


class UserObject(ObjectType):
    id = Int()
    first_name = String()
    last_name = String()
    username = String()
    password = String()
    salt = String()
    refresh_token = String()
    role_id = Int()
    role = Field(lambda: UserRoleObject)
    is_active = Boolean()
    created_at = String()
    updated_at = String()
    search = String()
