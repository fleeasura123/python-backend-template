from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.connection import Base


class UserRole(Base):
    __tablename__ = "user_roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
