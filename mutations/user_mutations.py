from graphene import Boolean, Mutation

from custom_decorators.authorize import authorize
from graphql_inputs.user.change_password import ChangePasswordInput
from repositories.user_repository import UserRepository


class ChangePassword(Mutation):
    class Arguments:
        input = ChangePasswordInput(required=True)

    success = Boolean()

    @authorize()
    async def mutate(self, info, input: ChangePasswordInput):
        await UserRepository().change_password(
            info.context["user"].id,
            input.old_password,
            input.new_password,
        )
        return ChangePassword(success=True)
