from backend.models.tasklists import TasklistModel
from backend.repository.base import BaseRepository
from backend.schemas import Tasklist
from uuid import UUID

class TasklistsRepository(BaseRepository):
    table = Tasklist

    def create(self, tasklist: TasklistModel) -> TasklistModel:
        return self.insert_and_return(self.table, tasklist.dict())

    def find_by_id(self, id: UUID) -> TasklistModel:
        return self.session.query(self.table)\
            .filter(self.table.id==id).first()

    def find_by_user_id(self, user_id: UUID):
        return self.session.query(self.table)\
            .filter(self.table.user_id==user_id).all()

    def delete_by_id(self, id: UUID) -> bool:
        self.session.query(self.table)\
            .filter(self.table.id==id).delete()
        self.session.commit()
        return True