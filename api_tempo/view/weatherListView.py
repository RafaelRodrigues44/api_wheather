from django.views import View
from django.shortcuts import render
from pymongo import MongoClient
from api_tempo.serializers.weatherSerializer import WeatherSerializer

class WeatherListView(View):
    serializer_class = WeatherSerializer

    def get(self, request):
        try:
            # Conecta-se ao MongoDB
            connection_string = "mongodb+srv://gkrcido:128Acido@cluster0.xglpozx.mongodb.net/"
            database_name = 'weather_rafaelRodrigues'
            client = MongoClient(connection_string)
            db = client[database_name]

            # Consulta todos os documentos da coleção de previsão do tempo
            weather_records = db.weather.find()

            # Serializa os dados das previsões do tempo
            serializer = WeatherSerializer(weather_records, many=True)

            # Renderiza a página HTML de template com os dados serializados
            return render(request, 'weather_list.html', {'weather_records': serializer.data})

        except Exception as e:
            # Em caso de erro, retorna uma resposta de erro
            return render(request, 'error.html', {'message': 'Erro ao processar a solicitação'})


