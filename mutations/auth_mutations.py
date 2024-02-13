from graphene import Field, Mutation
from graphql_inputs.auth.login import LoginInput
from graphql_inputs.auth.refresh_token import RefreshTokenInput
from graphql_types.tokens import TokenType

from repositories.auth_repository import AuthRepository


class Login(Mutation):
    class Arguments:
        input = LoginInput(required=True)

    tokens = Field(TokenType)

    async def mutate(self, info, input: LoginInput):
        tokens = await AuthRepository().login(input.username, input.password)
        return Login(tokens=tokens)


class RefreshToken(Mutation):
    class Arguments:
        input = RefreshTokenInput(required=True)

    tokens = Field(TokenType)

    async def mutate(self, info, input: RefreshTokenInput):
        tokens = await AuthRepository().refresh_token(input.refresh_token)
        return RefreshToken(tokens=tokens)
