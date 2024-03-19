import pymongo

from core import settings

class WeatherRepository:
  
    DATABASE_NAME = "weather_rafaelrodrigues"

    def __init__(self, collection_name="weather_collection") -> None:
        self.collection_name = collection_name
        self.connection = self.get_connection()

    def get_connection(self):
        client = pymongo.MongoClient(settings.MONGO_CONNECTION_STRING)
        connection = client[self.DATABASE_NAME]
        return connection

    def get_collection(self):
        conn = self.connection
        collection = conn[self.collection_name]
        return collection

    def get_all(self):
        collection = self.get_collection()
        documents = collection.find({})
        return documents

    def collection_exists(self):
        return self.collection.name in self.connection.list_collection_names()

    def create(self, weather):
        collection = self.get_collection()
        data = {
            'city': weather.city,
            'date': weather.date,
            'temperature': weather.temperature,
            'pressure': weather.pressure,
            'humidity': weather.humidity,
            'precipitation': weather.precipitation,
            'weather_condition': weather.weather_condition
        }
        collection.insert_one(data)

    