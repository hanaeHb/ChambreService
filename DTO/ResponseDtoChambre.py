class ResponseDtoChambre:
    def __init__(self, id: str, numero: str, type: str, prix: float, etat: str):
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
