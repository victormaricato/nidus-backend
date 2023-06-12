from backend.schemas import Settings
from typing import Optional
from pydantic import BaseModel
from backend.models.settings import Settings
from uuid import UUID

class UserInsert(BaseModel):
    id: UUID
    tw_id: str
    tw_name: str
    tw_access_token: str
    tw_access_token_verifier: str
    tw_profile_picture: str
    tw_email: str

class User(BaseModel):
    id: UUID
    tw_id: str
    tw_name: str
    tw_access_token: str
    tw_access_token_verifier: str
    tw_profile_picture: str
    tw_email: str
    settings: Settings

class NumberInsert(BaseModel):
    number: str