from graphene import InputObjectType, String


class LoginInput(InputObjectType):
    username = String(required=True)
    password = String(required=True)
