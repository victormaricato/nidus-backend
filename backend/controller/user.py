from backend.repository.user import UserRepository
from backend.repository.session import SessionRepository
from fastapi import APIRouter, Depends, Header

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
