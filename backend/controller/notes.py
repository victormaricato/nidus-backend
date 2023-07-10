from backend.repository.session import SessionRepository
from backend.repository.settings import SettingsRepository
from backend.models.notes import NoteModel, NoteInsert
from backend.repository.notes import NotesRepository
from backend.repository.user import UserRepository
from backend.service.tweet import post_tweet
from fastapi import APIRouter, Depends, Header, Request
from uuid import uuid4
import random

router = APIRouter(prefix="/notes")

@router.post("/")
async def post(
    note_insert: NoteInsert,
    authorization: str = Header(None),
    user_id: str = Header(None, convert_underscores=False),
    notes_repository: NotesRepository = Depends(),
    session_repository: SessionRepository = Depends(),
    user_repository: UserRepository = Depends(),
    settings_repository: SettingsRepository = Depends()
) -> NoteModel:
    if not session_repository.validate(authorization, user_id):
      return dict(error="Invalid token.")

    return notes_repository.create(NoteModel(
      id=uuid4(),
      user_id=user_id,
      content=note_insert.content,
    ))
