from graphene import ObjectType

from mutations.auth_mutations import Login, RefreshToken


class Mutation(ObjectType):
    login = Login.Field()
    refresh_token = RefreshToken.Field()
