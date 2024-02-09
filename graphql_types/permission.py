from graphene import Int, ObjectType, String, List, Field


class PermissionObject(ObjectType):
    id = Int()
    name = String()
