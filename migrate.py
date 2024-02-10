from db.connection import engine, Base

import sqlalchemy_models.user_role
import sqlalchemy_models.permission
import sqlalchemy_models.user_role_permission

Base.metadata.create_all(engine)
