from functools import wraps
from graphql import GraphQLError
import jwt
from datetime import datetime, timezone
from graphql_types.user import UserObject
from repositories.permission_repository import PermissionRepository


from utils.global_utils import get_config
from repositories.user_repository import UserRepository
from repositories.user_role_repository import UserRoleRepository


def authorize(permissions=[]):
    def wrapper(func):
        @wraps(func)
        async def wrapped(*args, **kwargs):
            info = args[1]

            request_object = info.context.get("request")

            authorization = request_object.headers.get("Authorization")

            if authorization is None:
                raise GraphQLError("Authorization header is required")

            if len(authorization.split(" ")) != 2:
                raise GraphQLError("Invalid authorization header format")

            token = authorization.split(" ")[1]

            config = get_config()

            try:
                payload = jwt.decode(
                    token,
                    config["TOKEN_SECRET_KEY"],
                    algorithms=[config["TOKEN_ALGORITHM"]],
                )
            except jwt.ExpiredSignatureError:
                raise GraphQLError("Token has expired")

            if datetime.now(timezone.utc) > datetime.fromtimestamp(
                payload["exp"], tz=timezone.utc
            ):
                raise GraphQLError("Token has expired")

            user_repository = UserRepository()
            user_role_repository = UserRoleRepository()
            permission_repository = PermissionRepository()

            user = await user_repository.get_by_id(payload["id"])

            if user is None:
                raise GraphQLError("User not found")

            user.role = await user_role_repository.get_single(user.role_id)

            user.role.permissions = await permission_repository.list_by_role_id(
                user.role_id
            )

            if len(permissions) > 0:
                user_permission_names = [
                    permission.name for permission in user.role.permissions
                ]

                for permission in permissions:
                    if permission not in user_permission_names:
                        raise GraphQLError(
                            f"You don't have permission to access this resource. Required permissions: {permissions}"
                        )

            info.context["user"] = user

            return await func(*args, **kwargs)

        return wrapped

    return wrapper
