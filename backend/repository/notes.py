from .base import BaseMongoRepository
from backend.models.notes import NoteModel


class NotesRepository(BaseMongoRepository):
    COLLECTION_NAME = "notes"

    def create(self, note: NoteModel) -> NoteModel:
        result = self.insert_and_return(note.dict(by_alias=True))
        return NoteModel(**result)
