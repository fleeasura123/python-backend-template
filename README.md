# Python GraphQL Codebase

This is a prototype codebase showcasing Python GraphQL functionality, leveraging FastAPI (https://pypi.org/project/fastapi/), Graphene (https://pypi.org/project/graphene/), and Psycopg3 (https://pypi.org/project/psycopg/). It includes essential features such as login, password modification, and robust authorization and authentication mechanisms.

# :file_folder: Folder Structure

custom_decorators
---
Place all custom decorators here.

graphql_inputs
---
Place all graphene inputs here, grouped by main feature/part.

For example:
```
graphql_inputs (folder)
-- auth (folder)
   -- login.py
-- user (folder)
   -- change_password.py
-- branch (folder)
   -- create.py
   -- update.py
   -- delete.py
```

```auth```, ```user```, and ```branch``` are the main features of the system.

graphql_types
---
Place all graphene types here.

mutations
---
Place all graphene mutations here, with one file per main feature/part.

For example:
```
auth_mutations.py --> contains all auth mutations, such as login, refresh_token, etc.

user_mutations.py --> contains all user mutations, such as create_user, update_user, change_password, etc.

branch_mutations.py --> contains all branch mutations, such as create_branch, update_branch, delete_branch, select_branch, get_single_branch, etc.
```

repositories
---
The repository is where you get data from the database, perform business logic, fetch from 3rd-party apps, etc.

Structure: one file per main feature/part.

For example:
```
user_repository.py --> Contains all user functions, such as get_all_user, get_single_user, update_user, delete_user, etc.

branch_repository.py --> Contains all branch functions.
```

utils
---
Place all utility functions here; there is no strict structure.

# Database Connection

Create a ```.env``` file in the root folder.

```
DB_PORT=5432
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_password
TOKEN_SECRET_KEY=your_jwt_secret_key
TOKEN_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRATION=3600
REFRESH_TOKEN_EXPIRATION=604800
```

This code uses a connection pool; you can change the pool max size in ```connection.py``` by modifying ```max_size``` from 80 to your preferred value.

```python
@lru_cache(maxsize=1)
def get_pool():
    return AsyncConnectionPool(
        conninfo=get_connection_settings(),
        check=AsyncConnectionPool.check_connection,
        max_size=80,
    )
```

# Authentication

This system uses JWT for authentication. Update the following values in your ```.env``` file:

```
TOKEN_SECRET_KEY=your_jwt_secret_key
TOKEN_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRATION=3600
REFRESH_TOKEN_EXPIRATION=604800
```
Expirations are in seconds. In the example above, the access_token will expire after 1 hour, and the refresh_token will expire after 7 days.

# Authorization

To understand how authorization works, consider the database structure:

permissions table
---
id | name

name = what we are using on authorization

examples: 
* create_user: permission for creating a user
* delete_user: permission for deleting a user

in the examples above, that is based on your preference, you are free to name your own permissions. For example: can_create_user etc...

user_roles table
---
id | name

id = we are using this on users table

user_roles have permissions, which can be inserted into the ```user_roles_permissions``` table.

examples:
* ID:1 name: Admin
    * can_create_user
    * can_update_user
    * can_delete_user
    * can_select_user

* ID:2 name: Staff
    * can_select_user 

users table
---
id | username | password | first_name | last_name | is_active | role_id | refresh_token | created_at | updated_at | salt | search

role_id is a foreign key of ```user_roles``` table

Explanation
---
Authorization works by assigning a role_id to the user. For example: assigning a role_id = 1 (Admin) grants admin permissions: can_create_user, can_update_user, can_delete_user, and can_select_user. If you assign role_id = 2 (Staff), the user has only the can_select_user permission.

# How to use Authentication

GraphQL is based on resolvers for selecting data and mutations for creating, updating, and deleting data. Protect resolvers and mutations by importing ```authorize.py``` from the custom_decorators folder.

To protect a resolver, add ```@authorize()``` above the resolver:

```python
@authorize()
async def resolve_roles(self, info):
    return await user_role_repository.get()
```

To protect a mutation, add ```@authorize()``` above the mutation:

```python
@authorize()
async def mutate(self, info, input: ChangePasswordInput):
    await UserRepository().change_password(
        info.context["user"].id,
        input.old_password,
        input.new_password,
    )
    return ChangePassword(success=True)
```
Users can access these resolvers and mutations by passing an ```Authorization``` header with a Bearer token:

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6OCwiZXhwIjoxNzA3ODM0MzQ0fQ.zl-Z2-OmM4ccH3YO0JJjHY1Z5Lz3PhRy1JHiiA4p16g
```

How to get the token?
---
You can get the token by logging in:

```
mutation Login($username:String!, $password:String!) {
  login(input: {username: $username, password: $password}) {
    tokens {
      accessToken
      refreshToken
    }
  }
}
```

After a successful login, you receive an ```accessToken``` and ```refreshToken```, which expire after a specified period of time according to your settings in ```.env```.

Refresh the token
---
If you pass an expired ```accessToken```, you will get an error, you can check it under extensions -> isTokenExpired:

```json
{
  "data": {
    "roles": null
  },
  "errors": [
    {
      "message": "Token has expired",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
      ],
      "path": [
        "roles"
      ],
      "extensions": {
        "isTokenExpired": true
      }
    }
  ]
}
```

You can refresh the access_token using the ```refresh_token mutation``` by passing the refreshToken you saved:

```
mutation RefreshToken($refreshToken: String!) {
  refreshToken (input: {refreshToken: $refreshToken}) {
    tokens {
      accessToken
      refreshToken
    }
  }
}
```

If the ```refreshToken``` has expired. You need to re-login.

How to get the authenticated user?
---
You can get it from the resolver or mutation context:

```python
info.context["user"]
```

# How to use Authorization?

Similar to authentication, use ```@authorize()``` but pass the required permission(s) like this:

```python
@authorize(["can_create_user"])
```

If the user does not have the ```can_create_user``` permission, it will raise an error.

You can also specify multiple permissions:

```python
@authorize(["get_user", "get_single_user"])
```

Custom Authorization Scenarios
---

Consider a scenario where the system has a ```branch``` and the user has a ```branch_id```.

branch represents entities like Jollibee, McDonald's, Burger King, etc. If there's a mutation to create a user, but the user can only create within their own branch_id, you can implement a custom solution like this:

```python
@authorize(["create_user"])
async def mutate(self, info, input: UserInput):
    ...
```

My own custom solution is doing something like this:

```python
@authorize(["create_user"])
async def mutate(self, info, input: UserInput):
    authenticated_user = info.context["user"]

    if(input.branch_id != authenticated_user.branch_id):
        raise GraphQLError("You cannot create a user on this branch")
```

Alternatively, change the branch_id of the input to match the authenticated user's branch_id:

```python
@authorize(["create_user"])
async def mutate(self, info, input: UserInput):
    authenticated_user = info.context["user"]

    input.branch_id = authenticated_user.branch_id
```