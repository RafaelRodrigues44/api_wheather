from django.shortcuts import redirect
from django.views import View
from api_tempo.models.weatherCollections import WeatherCollection  

class WeatherDeleteView(View):
    def get(self, request, pk):
        try:
            # Criar uma instância da classe WeatherCollection
            weather_collection = WeatherCollection()

            # Remover o documento da coleção MongoDB com base no ID fornecido
            weather_collection.delete_one({'_id': pk})

            # Redirecionar para a lista de previsões meteorológicas
            return redirect('weather-list')
        
        except Exception as e:
            # Em caso de erro, redirecionar para a lista de previsões meteorológicas com uma mensagem de erro
            return redirect('weather-list')
