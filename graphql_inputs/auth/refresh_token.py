from graphene import InputObjectType, String


class RefreshTokenInput(InputObjectType):
    refresh_token = String(required=True)
