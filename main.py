from fastapi import FastAPI, Request, HTTPException, Response
from datetime import datetime
from uuid import uuid4
from service_data import user_list, single_user
app = FastAPI()


@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    users = user_list()["data"]

    for user in users:
        if user["id"] == user_id:
            return {"data": user}

    raise HTTPException(status_code=404, detail="User not found")



@app.get("/api/users")
def get_user_list():
    return user_list()


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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
