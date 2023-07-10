from typing import Optional

from bson.objectid import ObjectId
from uuid import UUID
from pydantic import BaseModel, Field


class NoteModel(BaseModel):
    id: UUID
    tweet_id: Optional[str]
    user_id: str
    content: str


class NoteInsert(BaseModel):
    content: str
