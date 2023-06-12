from uuid import UUID
from pydantic import BaseModel
from typing import Optional

class TaskModel(BaseModel):
    id: UUID
    tasklist_id: UUID
    complete: bool
    content: str

class TasklistModel(BaseModel):
    id: UUID
    tweet_id: Optional[str]
    user_id: str
    content: str

class TasklistInsert(BaseModel):
    content: str
    tasks: list[str]


