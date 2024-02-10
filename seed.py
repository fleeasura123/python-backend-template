from connection import session
from sqlalchemy_models.permission import Permission
from sqlalchemy_models.user_role import UserRole
from sqlalchemy_models.user_role_permission import user_role_permission

# Create permissions
permissions = [
    Permission(id=1, name="create_user"),
    Permission(id=2, name="read_user"),
    Permission(id=3, name="update_user"),
    Permission(id=4, name="delete_user"),
    Permission(id=5, name="create_role"),
    Permission(id=6, name="read_role"),
    Permission(id=7, name="update_role"),
    Permission(id=8, name="delete_role"),
    Permission(id=9, name="create_permission"),
    Permission(id=10, name="read_permission"),
    Permission(id=11, name="update_permission"),
    Permission(id=12, name="delete_permission"),
]

# Create roles
roles = [
    UserRole(
        id=1,
        name="admin",
        permissions=[
            permissions[0],
            permissions[1],
            permissions[2],
            permissions[3],
            permissions[4],
            permissions[5],
            permissions[6],
            permissions[7],
            permissions[8],
            permissions[9],
            permissions[10],
            permissions[11],
        ],
    ),
    UserRole(
        id=2,
        name="user",
        permissions=[
            permissions[1],
            permissions[2],
            permissions[3],
            permissions[5],
            permissions[6],
            permissions[10],
        ],
    ),
]

session.query(Permission).delete()
session.query(UserRole).delete()
session.query(user_role_permission).delete()

session.add_all(permissions)
session.add_all(roles)

session.commit()
session.close()
