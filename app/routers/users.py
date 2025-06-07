from datetime import datetime

from fastapi import APIRouter, Request, HTTPException, Response, Query
from uuid import uuid4
#from app.main import USERS
from app.data.load_users import load_user_data
from app.models.models import PaginatedUsers

router = APIRouter(prefix="/api/users")
USERS = load_user_data()
@router.get("",response_model=PaginatedUsers)
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

@router.get("/{user_id}")
def get_user(user_id: int):
    for user in USERS:
        if user["id"] == user_id:
            return {"data": user}

    raise HTTPException(status_code=404, detail="User not found")



@router.post("")
async def create_user(request: Request):
    payload = await request.json()
    return {
        "name": payload.get("name"),
        "job": payload.get("job"),
        "id": str(uuid4()),
        "createdAt": datetime.utcnow().isoformat()
    }


@router.put("/{user_id}")
async def update_user(user_id: int, request: Request):
    payload = await request.json()
    return {
        "name": payload.get("name"),
        "job": payload.get("job"),
        "updatedAt": datetime.utcnow().isoformat()
    }


@router.delete("/{user_id}")
def delete_user(user_id: int):
    return Response(status_code=204)