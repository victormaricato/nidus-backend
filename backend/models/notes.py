from uuid import UUID
from pydantic import BaseModel
from typing import Optional

class NoteModel(BaseModel):
    id: UUID
    tweet_id: Optional[str]
    user_id: str
    content: str

class NoteInsert(BaseModel):
    content: str
