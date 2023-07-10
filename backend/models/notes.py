from typing import Optional

from bson.objectid import ObjectId
from pydantic import BaseModel, Field


class NoteModel(BaseModel):
    id: Optional[ObjectId] = Field(alias='_id')
    tweet_id: Optional[str]
    user_id: str
    content: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }


class NoteInsert(BaseModel):
    content: str
