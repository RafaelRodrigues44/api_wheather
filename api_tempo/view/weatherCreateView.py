from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from api_tempo.repositories import WeatherRepository
from api_tempo.serializers.weatherSerializer import WeatherSerializer


class WeatherInsert(View):
    def get(self, request):
        return render(request, "weather_create.html", {"show_form": True})

    def post(self, request):
        try:
            id = request.POST.get('id')  
            city = request.POST.get('city')
            date = request.POST.get('date')
            temperature = request.POST.get('temperature')
            atmosphericPressure = request.POST.get('atmosphericPressure')
            humidity = request.POST.get('humidity')
            weather = request.POST.get('weather')

            # Criação do dicionário de dados para serialização
            weather_data = {
                'id': id,  
                'city': city,
                'date': date,
                'temperature': temperature,
                'atmosphericPressure': atmosphericPressure,
                'humidity': humidity,
                'weather': weather
            }

            serializer = WeatherSerializer(data=weather_data)
            if serializer.is_valid():
                repository = WeatherRepository(collectionName='weathers')
                object_id = repository.insert(serializer.validated_data)
                return HttpResponseRedirect(reverse('weather-list'))
            else:
                return render(request, "weather_create.html", {"form": request.POST, "errors": serializer.errors, "show_form": True})

        except Exception as e:
            return render(request, "weather_.html", {"error_message": "Erro ao criar a previsão do tempo.", "show_form": True})
