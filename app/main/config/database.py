from pymongo.mongo_client import MongoClient
from .env import MONGO, DB_NAME, COLLECTION_NAME


class MongoConnection:
    def __init__(self):
        pass

    def __enter__(self):
        self.client = MongoClient(MONGO)
        try:
            self.client.admin.command('ping')
        except Exception:
            self.client.close()
            raise ConnectionError("Cannot connect to Mongo Database")
        database = self.client[DB_NAME]
        collection = database[COLLECTION_NAME]
        return collection

    def __exit__(self, exc_type, exc_value, traceback):
        self.client.close()
