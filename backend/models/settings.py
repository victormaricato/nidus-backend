from typing import Optional
from uuid import UUID
from pydantic import BaseModel

class SettingsInsert(BaseModel):
    id: str
    note: Optional[bool]
    task: Optional[bool]
    reminder: Optional[bool]
    email: Optional[bool]
    push: Optional[bool]
    user_id: str

class Settings(BaseModel):
    id: str
    note: bool
    task: bool
    reminder: bool
    email: bool
    push: bool
    user_id: str
