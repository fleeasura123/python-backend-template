from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from .models import Base
from .user_role_permission import user_role_permission


class Permission(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    roles = relationship(
        "UserRole", secondary=user_role_permission, back_populates="permissions"
    )
