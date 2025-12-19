from pymongo import MongoClient

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create/use database
db = client["hotel_management"]

# Collection chambres
chambres_collection = db["chambres"]
