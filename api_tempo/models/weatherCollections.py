from pymongo import MongoClient

class WeatherCollection:
    def __init__(self):
        self.connection_string = "mongodb+srv://gkrcido:128Acido@cluster0.xglpozx.mongodb.net/"
        self.database_name = 'weather_rafaelRodrigues'
        self.collection_name = 'weather'
        self.client = MongoClient(self.connection_string)
        self.db = self.client[self.database_name]
        self.collection = self.db[self.collection_name]

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
