from db.connection import session
from sqlalchemy_models.permission import Permission
from sqlalchemy_models.user_role import UserRole
from sqlalchemy_models.user_role_permission import UserRolePermission

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
    UserRole(id=1, name="admin"),
    UserRole(id=2, name="user"),
    UserRole(id=3, name="guest"),
]

# Create user_role_permission
user_role_permissions = [
    UserRolePermission(user_role_id=1, permission_id=1),
    UserRolePermission(user_role_id=1, permission_id=2),
    UserRolePermission(user_role_id=1, permission_id=3),
    UserRolePermission(user_role_id=1, permission_id=4),
    UserRolePermission(user_role_id=1, permission_id=5),
    UserRolePermission(user_role_id=1, permission_id=6),
    UserRolePermission(user_role_id=1, permission_id=7),
    UserRolePermission(user_role_id=1, permission_id=8),
    UserRolePermission(user_role_id=1, permission_id=9),
    UserRolePermission(user_role_id=1, permission_id=10),
    UserRolePermission(user_role_id=1, permission_id=11),
    UserRolePermission(user_role_id=1, permission_id=12),
    UserRolePermission(user_role_id=2, permission_id=2),
    UserRolePermission(user_role_id=2, permission_id=6),
    UserRolePermission(user_role_id=2, permission_id=10),
]

session.query(UserRolePermission).delete()
session.query(Permission).delete()
session.query(UserRole).delete()

session.add_all(permissions)
session.add_all(roles)
session.add_all(user_role_permissions)

session.commit()
session.close()
