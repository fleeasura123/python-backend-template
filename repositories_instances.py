from db.connection import session, Base

# Repositories
from repositories.user_role_repository import UserRoleRepository
from repositories.permission_repository import PermissionRepository

# Repositories instances
user_role_repository = UserRoleRepository(session, Base)
permission_repository = PermissionRepository(session, Base)
