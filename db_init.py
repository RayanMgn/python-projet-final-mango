from pymongo import MongoClient

def get_database():
    MONGO_URI = "mongodb://localhost:27017/"
    client = MongoClient(MONGO_URI)
    db = client["jeux_video"]
    return db


if __name__ == "__main__":
    db = get_database()
    print("Connexion MongoDB réussie.")
    print("Collections présentes :", db.list_collection_names())
