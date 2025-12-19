from Repository import ChambreRepository
from DTO import RequestDtoChambre
from Mapper.ChambreMapper import dto_to_entity
from Mapper.ChambreMapper import entity_to_dto
class ChambreService:
    def __init__(self, repository: ChambreRepository):
        self.repository = repository

    def add_chambre(self, dto: RequestDtoChambre):
        chambre = dto_to_entity(dto)
        self.repository.save(chambre)
        return entity_to_dto(chambre)

    def get_chambre(self, id: int):
        chambre = self.repository.find_by_id(id)
        return entity_to_dto(chambre) if chambre else None
