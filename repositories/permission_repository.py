from dotenv import dotenv_values

from sqlalchemy_models.permission import Permission
from sqlalchemy_models.user_role_permission import UserRolePermission

config = dotenv_values(".env")


class PermissionRepository:
    def __init__(self, session, base):
        self.session = session
        self.base = base

    def list(self):
        return self.session.query(Permission).all()

    def list_by_role(self, role_id, page):
        result = (
            self.session.query(Permission)
            .join(UserRolePermission)
            .filter_by(user_role_id=role_id)
            .order_by(Permission.name.desc())
            .offset((page - 1) * int(config["MAX_DATA_PER_PAGE"]))
            .limit(int(config["MAX_DATA_PER_PAGE"]))
            .all()
        )

        return result
