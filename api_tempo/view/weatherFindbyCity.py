from django.http import JsonResponse
from django.views import View
from api_tempo.models import Weather

class WeatherFindByCity(View):
    def get(self, request, city):
        # Filtra os registros de previsão do tempo pelo nome da cidade fornecido
        weather_records = Weather.objects.filter(city=city)
        
        # Verifica se existem registros para a cidade fornecida
        if weather_records.exists():
            # Serializa os dados das previsões do tempo
            weather_data = [{
                'id': record.id,
                'city': record.city,
                'temperature': record.temperature,
                # Adicione outros campos da previsão do tempo conforme necessário
            } for record in weather_records]
            
            # Retorna os dados das previsões do tempo em formato JSON
            return JsonResponse(weather_data, safe=False)
        else:
            # Se não houver registros para a cidade fornecida, retorna uma resposta vazia
            return JsonResponse({'message': 'No weather data found for the city provided'}, status=404)
