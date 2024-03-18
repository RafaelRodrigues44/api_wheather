from django.http import JsonResponse
from django.views import View
from api_tempo.models.weatherCollections import WeatherCollection  

class WeatherFindBy(View):
    def get(self, request, param):
        try:
            # Criar uma instância da classe WeatherCollection
            weather_collection = WeatherCollection()

            # Consultar os documentos de previsão do tempo com base no parâmetro fornecido
            if len(param) == 24:  # Verifica se o parâmetro é um ID válido
                # Consulta por ID
                weather_records = weather_collection.find_one({'_id': param})
            else:
                # Consulta por nome da cidade ou data e hora
                weather_records = weather_collection.find({'$or': [{'city': param}, {'date': param}]})

            # Verifica se existem registros para o parâmetro fornecido
            if weather_records:
                # Prepara os dados das previsões do tempo
                weather_data = [{
                    'id': str(record['_id']),
                    'city': record['city'],
                    'temperature': record['temperature'],
                    # Adicione outros campos da previsão do tempo conforme necessário
                } for record in weather_records]

                # Retorna os dados das previsões do tempo em formato JSON
                return JsonResponse(weather_data, safe=False)
            else:
                # Se não houver registros para o parâmetro fornecido, retorna uma resposta vazia
                return JsonResponse({'message': 'No weather data found for the provided parameter'}, status=404)
        
        except Exception as e:
            # Em caso de erro, retorna uma resposta de erro
            return JsonResponse({'message': 'An error occurred while processing the request'}, status=500)
