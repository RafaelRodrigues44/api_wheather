from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from api_tempo.repositories import WeatherRepository
from django.shortcuts import render

class WeatherGetView(View):
    def get(self, request, pk):
        repository = WeatherRepository(collectionName='weathers')
        try:
            weather_data = repository.get(pk)
            if weather_data:
                return render(request, 'weather_update.html', {'weather': weather_data, 'pk': pk})  # Passar pk para o template
            else:
                return HttpResponseBadRequest(f"Registro não encontrado para o ID: {pk}")
        except Exception as e:
            return HttpResponseBadRequest(f"Erro ao recuperar registro: {str(e)}")


class WeatherUpdateView(View):
    def post(self, request, pk):
        repository = WeatherRepository(collectionName='weathers')

        try:
            id = request.POST.get('id')  
            city = request.POST.get('city')
            date = request.POST.get('date')
            temperature = request.POST.get('temperature')
            atmosphericPressure = request.POST.get('atmosphericPressure')
            humidity = request.POST.get('humidity')
            weather = request.POST.get('weather')

            # Criação do dicionário de dados para serialização
            new_data = {
                'id': id,  
                'city': city,
                'date': date,
                'temperature': temperature,
                'atmosphericPressure': atmosphericPressure,
                'humidity': humidity,
                'weather': weather
            }

            # Atualizar no MongoDB
            repository.update(pk, new_data)

            return HttpResponseRedirect(reverse('weather-list'))
        except Exception as e:
            return HttpResponseBadRequest(f"Erro ao atualizar registro: {str(e)}")



      