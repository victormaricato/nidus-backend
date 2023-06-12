from uuid import UUID
from pydantic import BaseModel
from typing import Optional
from datetime import date

class ReminderModel(BaseModel):
    id: UUID
    tweet_id: Optional[str]
    date: str
    user_id: str
    content: str

class ReminderInsert(BaseModel):
    content: str
    date: str
