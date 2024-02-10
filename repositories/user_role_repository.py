from sqlalchemy_models.user_role import UserRole


class UserRoleRepository:
    def __init__(self, session, base):
        self.session = session
        self.base = base

    def list(self):
        return self.session.query(UserRole).all()
