from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")


def get_collection():
    client = MongoClient(MONGO_URI)
    db = client[f"{MONGO_DB}"]
    collection = db[f"{MONGO_COLLECTION}"]
    return collection
