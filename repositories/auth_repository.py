from graphql import GraphQLError
from psycopg.rows import class_row
import hashlib
import jwt
from datetime import datetime, timedelta

from connection import get_pool
from graphql_types.user import UserObject
from graphql_types.tokens import TokenObject
from utils.global_utils import get_config


class AuthRepository:

    def __init__(self) -> None:
        self.config = get_config()

    async def login(self, username: str, password: str):
        async with get_pool().connection() as connection:
            async with connection.cursor() as cursor:
                cursor.row_factory = class_row(UserObject)

                await cursor.execute(
                    """
                        SELECT
                            *
                        FROM
                            users
                        WHERE 
                            username = %(username)s
                            AND is_active = TRUE
                        LIMIT 1
                    """,
                    {"username": username},
                )

                user = await cursor.fetchone()

                if user is None:
                    raise GraphQLError("Invalid username or password")

                if user.password != self.hash_md5(password + user.salt):
                    raise GraphQLError("Invalid username or password")

                access_token_expiration = datetime.utcnow() + timedelta(
                    seconds=int(self.config["ACCESS_TOKEN_EXPIRATION"])
                )
                refresh_token_expiration = datetime.utcnow() + timedelta(
                    seconds=int(self.config["REFRESH_TOKEN_EXPIRATION"])
                )

                access_token = self.create_jwt(user, access_token_expiration)
                refresh_token = self.create_jwt(user, refresh_token_expiration)

                return TokenObject(
                    access_token=access_token,
                    refresh_token=refresh_token,
                )

    def hash_md5(self, input_string: str):
        return hashlib.md5(input_string.encode()).hexdigest()

    def create_jwt(self, user_id: int, expiration: datetime):
        return jwt.encode(
            {"id": user_id.id, "exp": expiration},
            self.config["TOKEN_SECRET_KEY"],
            algorithm=self.config["TOKEN_ALGORITHM"],
        )
