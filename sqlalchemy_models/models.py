from sqlalchemy.ext.declarative import declarative_base

from connection import engine

Base = declarative_base()

import sqlalchemy_models.permission
import sqlalchemy_models.user_role
import sqlalchemy_models.user_role_permission

Base.metadata.create_all(engine)
