
from fastapi import APIRouter
from http import HTTPStatus
from app.models.AppStatus import AppStatus

from app.database.engine import check_availability

router = APIRouter()
@router.get("/health", status_code=HTTPStatus.OK)
def health_check() -> AppStatus:
    return AppStatus(database=check_availability())