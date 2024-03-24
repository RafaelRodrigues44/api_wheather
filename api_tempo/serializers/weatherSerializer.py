from rest_framework import serializers
from api_tempo.repositories import WeatherRepository

class WeatherSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=255, allow_blank=True)  
    temperature = serializers.FloatField()
    date = serializers.DateTimeField()
    city = serializers.CharField(max_length=255, allow_blank=True)
    atmosphericPressure = serializers.FloatField(required=False)
    humidity = serializers.FloatField(required=False)
    weather = serializers.CharField(max_length=255, allow_blank=True)
    

    def create(self, validated_data):
        validated_data.pop('id', None)
        repository = WeatherRepository(collectionName='weathers')
        repository = repository.insert(validated_data)  
        return validated_data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['date'] = instance.get('date', '') 
        return representation