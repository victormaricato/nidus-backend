from backend.models.user import UserInsert, User
from backend.repository.base import BaseRepository
from backend.schemas import Settings, User
from uuid import UUID


class UserRepository(BaseRepository):
    table = User

    def __init__(self) -> None:
        super().__init__()

    def create(self, user: UserInsert) -> UUID:
        return self.insert(
            self.table,
            dict(**user.dict()),
        )

    def get_credentials(self, user_id: str):
        user = self.session.query(self.table)\
            .filter(self.table.id==user_id).first()
        return user.tw_access_token, user.tw_access_token_verifier

    def find_by_email(self, email: str) -> User:
        return self.session.query(self.table)\
            .filter(self.table.tw_email==email).first()

    def find_by_id(self, id: str) -> User:
        return self.session.query(self.table).join(self.table.settings)\
            .filter(self.table.id==id).first()

    def set_number(self,user_id: str, number: str):
        self.session.query(self.table)\
            .filter(self.table.id==user_id).first().phone = number
        self.session.commit()
        return True