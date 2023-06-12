from backend.models.reminders import ReminderModel
from backend.repository.base import BaseRepository
from backend.schemas import Reminder

class RemindersRepository(BaseRepository):
    table = Reminder

    def create(self, note: ReminderModel) -> ReminderModel:
        return self.insert_and_return(self.table, note.dict())