from pydantic import BaseModel


class UserRole(BaseModel):
    id: int
    name: str
