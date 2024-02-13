from graphene import Int, ObjectType, String


class TokenType(ObjectType):
    access_token = String()
    refresh_token = String()
