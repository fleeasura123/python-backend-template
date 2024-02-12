from graphene import Int, ObjectType, String


class PermissionObject(ObjectType):
    id = Int()
    name = String()
