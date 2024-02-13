from graphene import ObjectType

from mutations.auth_mutations import Login, RefreshToken
from mutations.user_mutations import ChangePassword


class Mutation(ObjectType):
    login = Login.Field()
    refresh_token = RefreshToken.Field()
    change_password = ChangePassword.Field()
