class Chambre:
    def __init__(self, id: int, numero: str, type: str, prix: float, etat: str):
        self.id = id
        self.numero = numero
        self.type = type
        self.prix = prix
        self.etat = etat

    def to_dict(self):
        return {
            "id": self.id,
            "numero": self.numero,
            "type": self.type,
            "prix": self.prix,
            "etat": self.etat
        }

    @staticmethod
    def from_dict(data: dict):
        return Chambre(
            id=data.get("id"),
            numero=data.get("numero"),
            type=data.get("type"),
            prix=data.get("prix"),
            etat=data.get("etat")
        )
