import json
from django.http import HttpResponseBadRequest
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from api_tempo.repositories import WeatherRepository
from api_tempo.models import WeatherModel
from api_tempo.serializers.weatherSerializer import WeatherSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class WeatherGetView(View):
    def get_object(self, pk):
        repository = WeatherRepository(collectionName='weathers')
        weather = repository.get(pk)
        return weather

    def get(self, request, pk):
        repository = WeatherRepository(collectionName='weathers')
        try:
            weather = repository.get(pk)
            serializer = WeatherSerializer(weather)
            return render(request, 'weather_update.html', {'weather': serializer.data, 'show_form': True, 'pk': pk})  # Passa o pk para o contexto do template
        except Exception as e:
            return HttpResponseBadRequest(f"Erro ao obter registro: {str(e)}")

class WeatherUpdateView(View):  
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, pk):
        try:
            # Convertendo os dados do corpo da requisição para um dicionário
            data = json.loads(request.body.decode('utf-8'))

            # Obtendo os dados do documento do MongoDB
            repository = WeatherRepository(collectionName='weathers')
            weather_data = repository.get(pk)

            # Criando uma instância de WeatherModel com os dados do MongoDB
            weather = WeatherModel(**weather_data)

            # Atualizando os campos do objeto com os dados recebidos
            weather.city = data.get('city', weather.city)
            weather.date = data.get('date', weather.date)
            weather.temperature = data.get('temperature', weather.temperature)
            weather.atmosphericPressure = data.get('atmosphericPressure', weather.atmosphericPressure)
            weather.humidity = data.get('humidity', weather.humidity)
            weather.weather = data.get('weather', weather.weather)

            # Salvando as alterações no banco de dados
            weather.save()

            # Convertendo o objeto WeatherModel para um dicionário
            weather_dict = {
                'id': weather.id,
                'temperature': weather.temperature,
                'city': weather.city,
                'atmosphericPressure': weather.atmosphericPressure,
                'humidity': weather.humidity,
                'weather': weather.weather,
                'date': weather.date.strftime('%Y-%m-%d %H:%M:%S')  # Formatando a data como string
            }

            # Retornando os dados atualizados como resposta JSON
            return JsonResponse(weather_dict)

        except Exception as e:
            # Retornando uma resposta de erro em caso de falha
            return JsonResponse({'error_message': f"Erro ao atualizar registro: {str(e)}"}, status=500)