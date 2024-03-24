from django.shortcuts import redirect, render
from django.views import View
from api_tempo.serializers.weatherSerializer import WeatherSerializer
from api_tempo.repositories import WeatherRepository
from api_tempo.models import WeatherModel

class WeatherInsert(View):
    def get(self, request):
        return render(request, "weather_create.html")
    
    def post(self, request):
        id = request.POST.get('id')
        city = request.POST.get('city')
        date = request.POST.get('date')
        temperature = request.POST.get('temperature')
        atmosphericPressure = request.POST.get('atmosphericPressure')
        humidity = request.POST.get('humidity')
        weather = request.POST.get('weather')

        # Remover o campo 'id' dos dados
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
            # Insira os dados e obtenha o ID gerado pelo MongoDB
            object_id = repository.insert(serializer.validated_data)
            # Redirecione para a lista de previsões meteorológicas
            return redirect('weather-list') 
        else:
            print(serializer.errors)

        return render(request, "weather_create.html", {"form": request.POST})
