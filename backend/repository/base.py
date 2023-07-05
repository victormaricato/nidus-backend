from typing import Dict, Any
from uuid import UUID

from bson.objectid import ObjectId
from pymongo import MongoClient
from sqlalchemy import Table, create_engine
from sqlalchemy.orm import sessionmaker

# DATABASE_URL: str = environ.get("CLEARDB_DATABASE_URL", "mysql://root:1234@127.0.0.1:3306/nidus")

DATABASE_URL: str = "mysql://root@localhost:3306/nidus"


class BaseRepository:
    def __init__(self):
        engine = create_engine(DATABASE_URL)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def insert(self, table: Table, values: Dict[str, Any]) -> UUID:
        obj_to_insert = table(**values)
        self.session.add(obj_to_insert)
        self.session.commit()
        return obj_to_insert.id

    def update(self, table: Table, id: UUID, values: Dict[str, Any]) -> bool:
        self.session.query(table).filter(table.id == id).update(values)
        self.session.commit()
        return True

    def insert_and_return(self, table: Table, values: Dict[str, Any]):
        obj_to_insert = table(**values)
        self.session.add(obj_to_insert)
        self.session.commit()
        # GAMBIARRA FOI FEITA
        # CORRIGE AQUI POR FAVOR VITAO
        return self.session.query(table) \
            .filter(table.id == obj_to_insert.id).first()


class BaseMongoRepository:
    DATABASE_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "nidus"

    def __init__(self):
        client = MongoClient(DATABASE_URL)
        self.db = client[self.DATABASE_NAME]
        self.collection = self.db[self.COLLECTION_NAME]

    def insert(self, values: Dict[str, Any]) -> ObjectId:
        result = self.collection.insert_one(values)
        return result.inserted_id

    def update(self, id: ObjectId, values: Dict[str, Any]) -> bool:
        self.collection.update_one({'_id': id}, {'$set': values})
        return True

    def insert_and_return(self, values: Dict[str, Any]) -> Dict:
        obj_id = self.insert(values)
        return self.collection.find_one({"_id": obj_id})
