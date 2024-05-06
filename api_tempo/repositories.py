from api_tempo.models.weatherModel import WeatherModel
from bson import ObjectId
from django.conf import settings
import pymongo

class WeatherRepository:
    def __init__(self, collectionName):
        self.collection = collectionName

    def getConnection(self):
        client = pymongo.MongoClient(getattr(settings, "MONGO_CONNECTION_STRING"))
        connection = client[getattr(settings, "MONGO_DATABASE_NAME")]
        return connection
    
    def getCollection(self):
        conn = self.getConnection()
        collection = conn[self.collection]
        return collection
    
    def getAll(self, city=None):
        query = {}
        if city:
            query['city'] = city
        
        documents = self.getCollection().find(query)
        return list(documents)
    
    def insert(self, document):
        self.getCollection().insert_one(document)

    def deleteAll(self):
        self.getCollection().delete_many({})

    def delete(self, document_id):
        self.getCollection().delete_one({'_id': ObjectId(document_id)})

    def update(self, document_id, new_data):
        self.getCollection().update_one({'_id': ObjectId(document_id)}, {'$set': new_data})

    def get(self, document_id):
        weather_data = self.getCollection().find_one({'_id': ObjectId(document_id)})
        if weather_data:
            # Criando uma instância de WeatherModel com os dados do MongoDB
            weather_model = WeatherModel(
                id=weather_data.get('id', None),
                temperature=weather_data['temperature'],
                city=weather_data['city'],
                atmosphericPressure=weather_data['atmosphericPressure'],
                humidity=weather_data['humidity'],
                weather=weather_data['weather'],
                date=weather_data['date']
            )
            return weather_model
        else:
            return None
