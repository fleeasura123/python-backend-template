from graphene import Int, ObjectType, String


class TokenObject(ObjectType):
    access_token = String()
    refresh_token = String()
