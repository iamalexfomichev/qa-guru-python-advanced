from fastapi import FastAPI, Request, HTTPException, Response, Query
from datetime import datetime
from uuid import uuid4
import json
import os
from pydantic import BaseModel
from typing import List

# Construct the absolute path to the JSON file
file_path = os.path.join(os.path.dirname(__file__), "service data", "user_list.json")

# Load the user data
with open(file_path, "r") as file:
    USERS = json.load(file)

# Определяем модель пользователя
class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

class PaginatedUsers(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[User]

# Создаем экземпляр FastAPI
app = FastAPI()

@app.get("/api/users", response_model=PaginatedUsers)
def get_users(page: int = Query(1, ge=1), per_page: int = Query(6, ge=1, le=100)):
    total = len(USERS)
    total_pages = (total + per_page - 1) // per_page
    if page > total_pages:
        raise HTTPException(status_code=404, detail="Page not found")
    start = (page - 1) * per_page
    end = start + per_page
    return {
        "page": page,
        "per_page": per_page,
        "total": total,
        "total_pages": total_pages,
        "data": USERS[start:end],
    }

@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    for user in USERS:
        if user["id"] == user_id:
            return {"data": user}

    raise HTTPException(status_code=404, detail="User not found")



@app.post("/api/users")
async def create_user(request: Request):
    payload = await request.json()
    return {
        "name": payload.get("name"),
        "job": payload.get("job"),
        "id": str(uuid4()),
        "createdAt": datetime.utcnow().isoformat()
    }


@app.put("/api/users/{user_id}")
async def update_user(user_id: int, request: Request):
    payload = await request.json()
    return {
        "name": payload.get("name"),
        "job": payload.get("job"),
        "updatedAt": datetime.utcnow().isoformat()
    }


@app.post("/api/register")
async def register_user(request: Request):
    payload = await request.json()

    if "email" not in payload or "password" not in payload:
        raise HTTPException(status_code=400, detail="Missing email or password")

    return {
        "id": 4,
        "token": "QpwL5tke4Pnpja7X4"
    }


@app.delete("/api/users/{user_id}")
def delete_user(user_id: int):
    return Response(status_code=204)

@app.get("/health")
def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
