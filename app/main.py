import dotenv
dotenv.load_dotenv()

from app.database.engine import create_db_and_tables
from fastapi import FastAPI, Request, HTTPException, Response, Query
from datetime import datetime

from uuid import uuid4
import json
import os
from pydantic import BaseModel
from typing import List
from models.models import User, PaginatedUsers
from routers import status, users
from data.load_users import load_user_data # Import the function to load user data


# Construct the absolute path to the JSON file

app = FastAPI()
app.include_router(status.router)
app.include_router(users.router)
# Load the user data

USERS = load_user_data()




@app.post("/api/register")
async def register_user(request: Request):
    payload = await request.json()

    if "email" not in payload or "password" not in payload:
        raise HTTPException(status_code=400, detail="Missing email or password")

    return {
        "id": 4,
        "token": "QpwL5tke4Pnpja7X4"
    }


if __name__ == "__main__":
    create_db_and_tables()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
