from backend.models.session import SessionInsert
from backend.repository.base import BaseRepository
from backend.schemas import Session
from datetime import datetime
from uuid import UUID

class SessionRepository(BaseRepository):
    table = Session

    def create(self, session: SessionInsert) -> UUID:
        # TODO: Precisa colocar active como falso
        # Para todos que corresponderem ao id do usuario e depois criar
        # Para evitar que exista mais de um token valido por user
        return self.insert(self.table, session.dict())

    def end_session(self, session_id: UUID) -> bool:
        return self.update(self.table, session_id, dict(end_at=datetime.utcnow))

    def validate(self, access_token: UUID, user_id: UUID) -> bool:
        if(access_token == None or user_id == None):
            return False
        
        # TODO: Precisa retornar somente token que estiver válido
        token = self.session.query(self.table)\
            .filter(self.table.access_token==access_token[7:]).first()
        
        if(token != None):
            if(str(token.user_id) == str(user_id) and token.active == True):
                return True
        
        print('Invalid credentials provided.')
        return False
