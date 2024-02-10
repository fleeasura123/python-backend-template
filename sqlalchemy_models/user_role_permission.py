from sqlalchemy import Table
from sqlalchemy import Column, ForeignKey, Integer

from db.connection import Base


class UserRolePermission(Base):
    __tablename__ = "user_roles_permissions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_role_id = Column(
        "user_role_id", Integer, ForeignKey("user_roles.id"), nullable=False, index=True
    )
    permission_id = Column(
        "permission_id",
        Integer,
        ForeignKey("permissions.id"),
        nullable=False,
        index=True,
    )
