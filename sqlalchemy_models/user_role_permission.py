from sqlalchemy import Table
from sqlalchemy import Column, ForeignKey, Integer, String

from .models import Base

user_role_permission = Table(
    "user_roles_permissions",
    Base.metadata,
    Column("user_role_id", Integer, ForeignKey("user_roles.id"), nullable=False),
    Column("permission_id", Integer, ForeignKey("permissions.id"), nullable=False),
)
