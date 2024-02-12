from graphene import Schema
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_playground_handler

from queries import Query

schema = Schema(query=Query)

app = FastAPI()

app.mount("/graphql", GraphQLApp(schema=schema, on_get=make_playground_handler()))
