# models.py
from pydantic import BaseModel, EmailStr, HttpUrl
from typing import List
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __table_args__ = {"extend_existing": True}
    id: int | None = Field(primary_key=True)
    email: str
    first_name: str
    last_name: str
    avatar: str



class UserCreate(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    avatar: HttpUrl | None = None


class UserUpdate(BaseModel):
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    avatar: str | None = None


class PaginatedUsers(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[User]
