from flask import Flask, request, jsonify
from db import chambres_collection

app = Flask(__name__)

# Hello World test
@app.route('/')
def hello_world():
    return "Hello World!"

# Add chambre (POST dynamic)
@app.route("/chambres", methods=["POST"])
def add_chambre():
    data = request.json
    if not data.get("numero") or not data.get("type"):
        return jsonify({"message": "Missing fields"}), 400

    # Auto id
    data["id"] = chambres_collection.count_documents({}) + 1

    # Insert f MongoDB
    result = chambres_collection.insert_one(data)

    # Convert ObjectId to string for response
    response_data = data.copy()
    response_data["_id"] = str(result.inserted_id)

    return jsonify({"message": "Chambre added!", "chambre": response_data}), 201


# Get all chambres
@app.route("/chambres", methods=["GET"])
def get_chambres():
    chambres = list(chambres_collection.find({}, {"_id": 0}))
    return jsonify(chambres), 200

# Get chambre by id
@app.route("/chambres/<int:id>", methods=["GET"])
def get_chambre(id):
    chambre = chambres_collection.find_one({"id": id}, {"_id": 0})
    if chambre:
        return jsonify(chambre), 200
    return jsonify({"message": "Chambre not found"}), 404

# Update chambre by id
@app.route("/chambres/<int:id>", methods=["PUT"])
def update_chambre(id):
    data = request.json
    chambres_collection.update_one({"id": id}, {"$set": data})
    return jsonify({"message": "Chambre updated"}), 200

# Delete chambre by id
@app.route("/chambres/<int:id>", methods=["DELETE"])
def delete_chambre(id):
    chambres_collection.delete_one({"id": id})
    return jsonify({"message": "Chambre deleted"}), 200

# Change état chambre by id
@app.route("/chambres/<int:id>/etat", methods=["PATCH"])
def changer_etat(id):
    # Jib chambre mn MongoDB
    chambre = chambres_collection.find_one({"id": id})
    if not chambre:
        return jsonify({"message": "Chambre not found"}), 404

    # Tbdl l'état
    nouveau_etat = "occupée" if chambre.get("etat") == "libre" else "libre"
    chambres_collection.update_one({"id": id}, {"$set": {"etat": nouveau_etat}})

    return jsonify({"message": "État changé", "id": id, "nouvel_etat": nouveau_etat}), 200

# Run app
if __name__ == "__main__":
    print("Starting Flask app on port 8088...")
    app.run(debug=True, port=8088)
