from typing import Optional, List

class ResponseDtoChambre:
    def __init__(self, id: str, numero: str, type: str, prix: float, etat: str, description: Optional[str] = None,
                 image_urls: Optional[List[str]] = None,
                 taux: Optional[float] = None,  reservation_id: Optional[int] = None,
                 housekeeping_ids: Optional[List[int]] = None,
                 maintenance_ids: Optional[List[int]] = None):
        self.id = id
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

    def to_dict(self):
        return {
            "id": self.id,
            "numero": self.numero,
            "type": self.type,
            "prix": self.prix,
            "etat": self.etat,
            "description": self.description,
            "image_urls": self.image_urls,
            "taux": self.taux,
            "reservation_id": self.reservation_id,
            "housekeeping_ids": self.housekeeping_ids,
            "maintenance_ids": self.maintenance_ids,
        }
