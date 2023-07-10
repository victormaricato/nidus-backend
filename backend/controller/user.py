from sqlalchemy.sql.functions import user
from backend.repository.user import UserRepository
from backend.repository.session import SessionRepository
from backend.models.user import NumberInsert
from fastapi import APIRouter, Depends, Header
from typing import Any, Dict

router = APIRouter(prefix="/user")

@router.get("/")
async def get(user_id: str,
authorization: str = Header(None),
user_repository: UserRepository = Depends(),
session_repository: SessionRepository = Depends()
):
    if(session_repository.validate(authorization, user_id)):
        return user_repository.find_by_id(user_id)
    return dict(error="Invalid token.")

@router.post("/number")
async def set_number(
number_insert: NumberInsert, 
user_id: str = Header(None, convert_underscores=False),
authorization: str = Header(None),
user_repository: UserRepository = Depends(),
session_repository: SessionRepository = Depends()
):
    if(not(session_repository.validate(authorization, user_id))):
        return dict(error="Invalid token.")

    return user_repository.set_number(user_id, number_insert.number)