from .base import BaseRepository
from models.notes import NoteModel


class NotesRepository(BaseRepository):
    COLLECTION_NAME = "notes"

    def create(self, note: NoteModel) -> NoteModel:
        result = self.insert_and_return(note.dict(by_alias=True))
        return NoteModel(**result)
