class RequestDtoChambre:
    def __init__(self, numero: str, type: str, prix: float, etat: str):
        self.numero = numero
        self.type = type
        self.prix = prix
        self.etat = etat

    @staticmethod
    def from_dict(data: dict):
        return RequestDtoChambre(
            numero=data.get("numero"),
            type=data.get("type"),
            prix=data.get("prix"),
            etat=data.get("etat")
        )
