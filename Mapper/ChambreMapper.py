from Domain.Module.Chambre import Chambre
from DTO.RequestDtoChambre import RequestDtoChambre
from DTO.ResponseDtoChambre import ResponseDtoChambre

def dto_to_entity(dto: RequestDtoChambre) -> Chambre:
    return Chambre(
        id=None,
        numero=dto.numero,
        type=dto.type,
        prix=dto.prix,
        etat=dto.etat,
        description=dto.description,
        image_urls=dto.image_urls,
        taux=dto.taux,
        reservation_id=getattr(dto, "reservation_id", None),
        housekeeping_ids=getattr(dto, "housekeeping_ids", []),
        maintenance_ids=getattr(dto, "maintenance_ids", [])
    )

def entity_to_dto(entity: Chambre) -> ResponseDtoChambre:
    return ResponseDtoChambre(
        id=entity.id,
        numero=entity.numero,
        type=entity.type,
        prix=entity.prix,
        etat=entity.etat,
        description=entity.description,
        image_urls=entity.image_urls,
        taux=entity.taux,
        reservation_id=entity.reservation_id,
        housekeeping_ids=entity.housekeeping_ids,
        maintenance_ids=entity.maintenance_ids
    )
