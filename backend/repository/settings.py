from backend.models.settings import SettingsInsert
from backend.repository.base import BaseRepository
from backend.schemas import Settings
from uuid import UUID

class SettingsRepository(BaseRepository):
    table = Settings

    def create(self, settings: SettingsInsert) -> str:
        return self.insert(self.table, settings.dict())

    def update_settings(self, settings: Settings) -> Settings:
        self.update(self.table, settings.id, settings.dict())
        return self.find_by_id(settings.id)

    def find_by_id(self, id: UUID) -> Settings:
        return self.session.query(self.table)\
            .filter(self.table.id==id).first()
    
    def find_by_user_id(self, user_id: UUID) -> Settings:
        return self.session.query(self.table)\
            .filter(self.table.user_id==user_id).first()