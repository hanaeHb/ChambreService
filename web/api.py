from flask import Flask, request
from config.security import require_role
from flask_restx import Api, Resource, fields
from db import chambres_collection

app = Flask(__name__)

# Config Swagger avec JWT Bearer
authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': 'Bearer <JWT token>'
    }
}

api = Api(
    app,
    version="1.0",
    title="Chambre API",
    description="API gestion des chambres",
    authorizations=authorizations,
    security='Bearer Auth'
)

# Modèle pour Swagger
chambre_model = api.model('Chambre', {
    'id': fields.Integer(readOnly=True, description='ID de la chambre'),
    'numero': fields.String(required=True, description='Numéro de la chambre'),
    'type': fields.String(required=True, description='Type de chambre'),
    'prix': fields.Float(required=True, description='Prix de la chambre'),
    'etat': fields.String(required=True, description='État de la chambre'),
    'reservation_id': fields.Integer(description='ID de réservation'),
    'housekeeping_ids': fields.List(fields.Integer, description='IDs housekeeping'),
    'maintenance_ids': fields.List(fields.Integer, description='IDs maintenance')
})

# Namespace
ns = api.namespace('chambres', description='Opérations sur les chambres')

# Routes
@ns.route('/')
class ChambreList(Resource):
    @ns.marshal_list_with(chambre_model)
    def get(self):
        """Lister toutes les chambres"""
        chambres = list(chambres_collection.find({}, {"_id": 0}))
        return chambres

    @ns.expect(chambre_model)
    @ns.marshal_with(chambre_model, code=201)
    @api.doc(security='Bearer Auth')
    @require_role("ADMIN")
    def post(self):
        """Ajouter une chambre (ADMIN seulement)"""
        data = request.json
        data["id"] = chambres_collection.count_documents({}) + 1
        result = chambres_collection.insert_one(data)
        data["_id"] = str(result.inserted_id)
        return data, 201

@ns.route('/<int:id>')
class Chambre(Resource):
    @ns.marshal_with(chambre_model)
    def get(self, id):
        """Récupérer une chambre par ID"""
        chambre = chambres_collection.find_one({"id": id}, {"_id": 0})
        if chambre:
            return chambre
        api.abort(404, "Chambre non trouvée")

    @api.doc(security='Bearer Auth')
    @require_role("ADMIN")
    def put(self, id):
        """Mettre à jour une chambre (ADMIN seulement)"""
        data = request.json
        chambres_collection.update_one({"id": id}, {"$set": data})
        return {"message": "Chambre updated"}, 200

    @api.doc(security='Bearer Auth')
    @require_role("ADMIN")
    def delete(self, id):
        """Supprimer une chambre (ADMIN seulement)"""
        chambres_collection.delete_one({"id": id})
        return {"message": "Chambre deleted"}, 200

@ns.route('/<int:id>/etat')
class ChambreEtat(Resource):
    @api.doc(security='Bearer Auth')
    @require_role("ADMIN")
    def patch(self, id):
        """Changer l'état d'une chambre (ADMIN seulement)"""
        chambre = chambres_collection.find_one({"id": id})
        if not chambre:
            api.abort(404, "Chambre non trouvée")
        nouveau_etat = "occupée" if chambre.get("etat") == "libre" else "libre"
        chambres_collection.update_one({"id": id}, {"$set": {"etat": nouveau_etat}})
        return {"message": "État changé", "id": id, "nouvel_etat": nouveau_etat}, 200

# Run app
if __name__ == "__main__":
    app.run(debug=True, port=8088)
