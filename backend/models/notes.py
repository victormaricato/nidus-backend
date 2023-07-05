from typing import Optional

from bson.objectid import ObjectId
from pydantic import BaseModel, Field


class NoteModel(BaseModel):
    id: Optional[ObjectId] = Field(alias='_id')
    tweet_id: Optional[str]
    user_id: str
    content: str


class NoteInsert(BaseModel):
    content: str
