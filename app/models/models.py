# models.py
from pydantic import BaseModel, EmailStr
from typing import List
from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    email: EmailStr
    first_name: str
    last_name: str
    avatar: str

class PaginatedUsers(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[User]
