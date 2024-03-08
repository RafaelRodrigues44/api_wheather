from rest_framework import serializers
from api_tempo.models.weatherModel import Weather

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['id', 'city', 'date', 'temperature', 'pressure', 'humidity', 'precipitation', 'weather_condition']
