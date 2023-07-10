from .base import BaseMongoRepository
from backend.models.notes import NoteModel


class NotesRepository(BaseMongoRepository):
    COLLECTION_NAME = "notes"

    def create(self, note: NoteModel) -> NoteModel:
        result = self.insert_and_return(note.dict(by_alias=True))
        return NoteModel(**result)

    def find_by_user_id(self, user_id: str) -> list[NoteModel]:
        result = self.collection.find({"user_id": user_id})
        return [NoteModel(**note) for note in result]
