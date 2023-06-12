from backend.models.tasklists import TaskModel
from backend.repository.base import BaseRepository
from backend.schemas import Task

class TasksRepository(BaseRepository):
    table = Task

    def create(self, note: TaskModel) -> TaskModel:
        return self.insert_and_return(self.table, note.dict())