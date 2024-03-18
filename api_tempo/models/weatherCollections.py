from pymongo import MongoClient
from core import settings

class WeatherCollection:
    def __init__(self):
        mongo_settings = settings.DATABASES['default']
        mongo_uri = f"mongodb+srv://{mongo_settings['USERNAME']}:{mongo_settings['PASSWORD']}@{mongo_settings['HOST']}/{mongo_settings['NAME']}"
        self.client = MongoClient(mongo_uri)
        self.db = self.client[mongo_settings['NAME']]

    def insert(self, data):
        self.collection.insert_one(data)

    def find(self, query):
        return self.collection.find(query)

    def find_one(self, query):
        return self.collection.find_one(query)

    def update_one(self, query, data):
        self.collection.update_one(query, {'$set': data})

    def delete_one(self, query):
        self.collection.delete_one(query)
