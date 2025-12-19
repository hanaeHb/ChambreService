from pymongo import MongoClient
from Domain.Module.Chambre import Chambre
class ChambreRepository:
    def __init__(self, db):
        self.collection = db['chambres']

    def save(self, chambre: Chambre):
        self.collection.insert_one(chambre.to_dict())

    def find_by_id(self, id: int):
        data = self.collection.find_one({"id": id})
        return Chambre.from_dict(data) if data else None

    def update(self, id: int, chambre: Chambre):
        self.collection.update_one({"id": id}, {"$set": chambre.to_dict()})

    def delete(self, id: int):
        self.collection.delete_one({"id": id})
