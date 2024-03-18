from rest_framework import serializers
from pymongo import MongoClient
from bson import ObjectId

class WeatherSerializer(serializers.Serializer):
    city = serializers.CharField(max_length=100)
    date = serializers.DateTimeField()
    temperature = serializers.FloatField()
    pressure = serializers.FloatField()
    humidity = serializers.FloatField()
    precipitation = serializers.FloatField()
    weather_condition = serializers.CharField(max_length=100)

    def create(self, validated_data):
        # Conectar-se ao MongoDB
        client = MongoClient("mongodb://localhost:27017/")
        db = client["weather_database"]
        weather_collection = db["weather"]

        # Inserir os dados validados no MongoDB
        result = weather_collection.insert_one(validated_data)
        
        # Retorna o ID do documento inserido
        return str(result.inserted_id)

    def update(self, instance_id, validated_data):
        # Conectar-se ao MongoDB
        client = MongoClient("mongodb://localhost:27017/")
        db = client["weather_database"]
        weather_collection = db["weather"]

        # Atualizar o documento no MongoDB
        filter_query = {"_id": ObjectId(instance_id)}
        update_query = {"$set": validated_data}
        weather_collection.update_one(filter_query, update_query)

        # Retorna os dados atualizados
        return validated_data

    def delete(self, instance_id):
        # Conectar-se ao MongoDB
        client = MongoClient("mongodb://localhost:27017/")
        db = client["weather_database"]
        weather_collection = db["weather"]

        # Excluir o documento do MongoDB
        filter_query = {"_id": ObjectId(instance_id)}
        weather_collection.delete_one(filter_query)

        # Retorna True se a exclusão for bem-sucedida
        return True
