from graphene import Int, ObjectType, String


class PermissionType(ObjectType):
    id = Int()
    name = String()
