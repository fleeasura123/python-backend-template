from graphene import InputObjectType, String


class ChangePasswordInput(InputObjectType):
    old_password = String(required=True)
    new_password = String(required=True)
