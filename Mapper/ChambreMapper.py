from Domain.Module.Chambre import Chambre
from DTO.RequestDtoChambre import RequestDtoChambre
from DTO.ResponseDtoChambre import ResponseDtoChambre

def dto_to_entity(dto: RequestDtoChambre) -> Chambre:
    return Chambre(
        id=None,
        numero=dto.numero,
        type=dto.type,
        prix=dto.prix,
        etat=dto.etat
    )

def entity_to_dto(entity: Chambre) -> ResponseDtoChambre:
    return ResponseDtoChambre(
        id=entity.id,
        numero=entity.numero,
        type=entity.type,
        prix=entity.prix,
        etat=entity.etat
    )
