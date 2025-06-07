
from sqlmodel import Session, select
from .engine import engine
from ..models.models import User, PaginatedUsers
from typing import Iterable

def get_user(user_id: int):
    """
    Retrieve a user by ID from the database.
    """
    with Session(engine) as session:
        return session.get(User, user_id)

def get_users() -> Iterable[User]:
    """
    Retrieve all users from the database.
    """
    with Session(engine) as session:
        statement = select(User)
        return session.exec(statement).all()