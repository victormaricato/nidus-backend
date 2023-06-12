from typing import Optional
from pydantic import BaseModel
from uuid import UUID

class SessionInsert(BaseModel):
    id: UUID
    user_id: UUID
    access_token: UUID
    active: bool


class SessionEnd(BaseModel):
    id: UUID

class Session(BaseModel):
    id: UUID
    user_id: UUID
    access_token: UUID
    active: bool