from typing import Optional
from uuid import UUID
from pydantic import BaseModel

class SettingsInsert(BaseModel):
    id: UUID
    note: Optional[bool]
    task: Optional[bool]
    reminder: Optional[bool]
    email: Optional[bool]
    push: Optional[bool]
    user_id: UUID

class Settings(BaseModel):
    id: UUID
    note: bool
    task: bool
    reminder: bool
    email: bool
    push: bool
    user_id: UUID
