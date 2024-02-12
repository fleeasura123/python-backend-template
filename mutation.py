from graphene import ObjectType

from mutations.auth_mutations import Login


class Mutation(ObjectType):
    login = Login.Field()
