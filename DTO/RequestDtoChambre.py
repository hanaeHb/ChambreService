from typing import Optional, List

class RequestDtoChambre:
    def __init__(self, numero: str, type: str, prix: float, etat: str,  description: Optional[str] = None,
                 image_urls: Optional[List[str]] = None,
                 taux: Optional[float] = None,  reservation_id: Optional[int] = None,
                 housekeeping_ids: Optional[List[int]] = None,
                 maintenance_ids: Optional[List[int]] = None):
        self.numero = numero
        self.type = type
        self.prix = prix
        self.etat = etat
        self.description = description
        self.image_urls = image_urls
        self.taux = taux  # rating (ex: 4.5)
        self.reservation_id = reservation_id          # One-to-One
        self.housekeeping_ids = housekeeping_ids or []  # Many-to-Many
        self.maintenance_ids = maintenance_ids or []    # Many-to-Many

    @staticmethod
    def from_dict(data: dict):
        return RequestDtoChambre(
            numero=data.get("numero"),
            type=data.get("type"),
            prix=data.get("prix"),
            etat=data.get("etat"),
            description=data.get("description"),
            image_urls=data.get("image_urls"),
            taux=data.get("taux"),
            reservation_id=data.get("reservation_id"),
            housekeeping_ids=data.get("housekeeping_ids", []),
            maintenance_ids=data.get("maintenance_ids", []),
        )
