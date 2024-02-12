from graphene import Field, Mutation
from graphql_inputs.auth.login import LoginInput
from graphql_types.tokens import TokenObject


class Login(Mutation):
    class Arguments:
        input = LoginInput(required=True)

    tokens = Field(TokenObject)

    async def mutate(self, info, input: LoginInput):
        tokens = TokenObject(access_token="12345", refresh_token="6789")
        return Login(tokens=tokens)
