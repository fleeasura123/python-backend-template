from sqlalchemy_models.user_role import UserRole


class UserRoleRepository:
    def __init__(self, session):
        self.session = session

    def list(self):
        return self.session.query(UserRole).all()
