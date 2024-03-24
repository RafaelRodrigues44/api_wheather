from django.shortcuts import render
from django.views import View
from bson import ObjectId  
from api_tempo.repositories import WeatherRepository
from api_tempo.serializers.weatherSerializer import WeatherSerializer


class WeatherView(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        weathers = list(repository.getAll())

        # Convertendo o ObjectId para string
        for item in weathers:
            item['id'] = str(item['_id'])
            
        serializer = WeatherSerializer(data=weathers, many=True)
        
        
        if serializer.is_valid():
            return render(request, "weather_list.html", {"weather_records": serializer.data})
        else:
            print(serializer.errors)
            return render(request, "weather_list.html", {"weather_records": []})