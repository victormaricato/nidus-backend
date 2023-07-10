from backend.repository.session import SessionRepository
from backend.models.settings import Settings
from backend.repository.settings import SettingsRepository
from fastapi import APIRouter, Depends, Header, Request

router = APIRouter(prefix="/settings")


@router.put("/")
async def update(
    settings: Settings,
    authorization: str = Header(None),
    settings_repository: SettingsRepository = Depends(),
    session_repository: SessionRepository = Depends()
) -> Settings:
    if(session_repository.validate(authorization, settings.user_id)):
        return settings_repository.update_settings(settings)
    return dict(error="Invalid token.")

@router.get("/")
async def get(user_id: str,
authorization: str = Header(None),
settings_repository: SettingsRepository = Depends(),
session_repository: SessionRepository = Depends()
):
    if(session_repository.validate(authorization, user_id)):
        return settings_repository.find_by_user_id(user_id)
    return dict(error="Invalid token.")

    