from graphene import Schema, ObjectType, List
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_playground_handler

from graphql_types.user import UserObject


class Query(ObjectType):
    users = List(UserObject)

    def resolve_users(self, info):
        return []


schema = Schema(query=Query)

app = FastAPI()

app.mount("/graphql", GraphQLApp(schema=schema, on_get=make_playground_handler()))
