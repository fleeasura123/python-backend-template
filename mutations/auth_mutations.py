from graphene import Field, Mutation
from graphql_inputs.auth.login import LoginInput
from graphql_types.tokens import TokenObject

from repositories.auth_repository import AuthRepository


class Login(Mutation):
    class Arguments:
        input = LoginInput(required=True)

    tokens = Field(TokenObject)

    async def mutate(self, info, input: LoginInput):
        tokens = await AuthRepository().login(input.username, input.password)
        return Login(tokens=tokens)
