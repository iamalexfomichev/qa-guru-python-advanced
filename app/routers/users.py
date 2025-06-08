from datetime import datetime
from http import HTTPStatus
from typing import Iterable

from app.database import users
from fastapi import APIRouter, Request, HTTPException, Response
from uuid import uuid4

#from app.data.load_users import load_user_data
from app.models.models import User, UserCreate, UserUpdate

router = APIRouter(prefix="/api/users")
#USERS = load_user_data()
@router.get("", status_code=HTTPStatus.OK)
def get_users() -> Iterable[User]:
    return users.get_users()

@router.get("/{user_id}", status_code=HTTPStatus.OK)
def get_user(user_id: int) -> User:
    if user_id < 1:
        return HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="Invalid user")
    user = users.get_user(user_id)

    if user is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    return user



@router.post("", status_code=HTTPStatus.CREATED)
def create_user(user: User) -> User:
    UserCreate.model_validate(user)
    return users.create_user()

@router.put("/{user_id}", status_code=HTTPStatus.OK)
def update_user(user_id: int, user: User) -> User:
    if user_id < 1:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="Invalid user id")
    UserUpdate.model_validate(user.model_dump())
    return users.update_user(user_id, user)

@router.delete("/{user_id}", status_code=HTTPStatus.OK)
def delete_user(user_id: int):
    if user_id < 1:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="Invalid user id")
    users.delete_user(user_id)
    return {"message": "User deleted"}