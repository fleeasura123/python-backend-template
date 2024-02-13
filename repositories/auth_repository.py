from graphql import GraphQLError
from psycopg.rows import class_row
import hashlib
import jwt
from datetime import datetime, timedelta, timezone

from connection import get_pool
from graphql_types.user import UserType
from graphql_types.tokens import TokenType
from utils.global_utils import get_config


class AuthRepository:

    def __init__(self) -> None:
        self.config = get_config()

    async def login(self, username: str, password: str) -> TokenType:
        async with get_pool().connection() as connection:
            async with connection.cursor() as cursor:
                cursor.row_factory = class_row(UserType)

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
                        FOR UPDATE
                    """,
                    {"username": username},
                )

                user = await cursor.fetchone()

                if user is None:
                    raise GraphQLError(
                        "Invalid username or password",
                    )

                if user.password != self.hash_md5(password + user.salt):
                    raise GraphQLError("Invalid username or password")

                access_token = self.create_access_token(user.id)

                refresh_token = None

                if user.refresh_token is not None:
                    refresh_token = user.refresh_token

                    if self.validate_refresh_token(refresh_token) == None:
                        refresh_token = None

                if refresh_token is None:
                    refresh_token = self.create_refresh_token(user.id)

                await cursor.execute(
                    """
                        UPDATE
                            users
                        SET
                            refresh_token = %(refresh_token)s
                        WHERE
                            id = %(id)s
                    """,
                    {"refresh_token": refresh_token, "id": user.id},
                )

                return TokenType(
                    access_token=access_token,
                    refresh_token=refresh_token,
                )

    async def refresh_token(self, refresh_token: str) -> TokenType:
        payload = self.validate_refresh_token(refresh_token)

        if payload is None:
            raise GraphQLError("Token has expired", extensions={"isTokenExpired": True})

        access_token = self.create_access_token(payload["id"])

        return TokenType(
            access_token=access_token,
            refresh_token=refresh_token,
        )

    def hash_md5(self, input_string: str) -> str:
        return hashlib.md5(input_string.encode()).hexdigest()

    def create_access_token(self, user_id: int) -> str:
        expiration = datetime.utcnow() + timedelta(
            seconds=int(self.config["ACCESS_TOKEN_EXPIRATION"])
        )

        return self.create_jwt(user_id, expiration)

    def create_refresh_token(self, user_id: int) -> str:
        expiration = datetime.utcnow() + timedelta(
            seconds=int(self.config["REFRESH_TOKEN_EXPIRATION"])
        )

        return self.create_jwt(user_id, expiration)

    def create_jwt(self, user_id: int, expiration: datetime) -> str:
        return jwt.encode(
            {"id": user_id, "exp": expiration},
            self.config["TOKEN_SECRET_KEY"],
            algorithm=self.config["TOKEN_ALGORITHM"],
        )

    def validate_refresh_token(self, refresh_token: str) -> None | str:
        payload = None

        try:
            payload = jwt.decode(
                refresh_token,
                self.config["TOKEN_SECRET_KEY"],
                algorithms=[self.config["TOKEN_ALGORITHM"]],
            )
        except jwt.ExpiredSignatureError:
            return None

        if payload is not None:
            if datetime.now(timezone.utc) > datetime.fromtimestamp(
                payload["exp"], tz=timezone.utc
            ):
                return None

        return payload
