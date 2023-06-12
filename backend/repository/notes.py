from backend.models.notes import NoteModel
from backend.repository.base import BaseRepository
from backend.schemas import Note

class NotesRepository(BaseRepository):
    table = Note

    def create(self, note: NoteModel) -> NoteModel:
        return self.insert_and_return(self.table, note.dict())