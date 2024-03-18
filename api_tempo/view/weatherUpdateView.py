from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from pymongo import MongoClient
from datetime import datetime
from api_tempo.serializers.weatherSerializer import WeatherSerializer

class WeatherUpdateView(View):
    template_name = 'weather_edit.html'

    def get(self, request, pk):
        try:
            # Conecta-se ao MongoDB
            connection_string = "mongodb+srv://gkrcido:128Acido@cluster0.xglpozx.mongodb.net/"
            database_name = 'weather_rafaelRodrigues'
            client = MongoClient(connection_string)
            db = client[database_name]

            # Encontra o documento de previsão do tempo com base no ID fornecido
            weather_record = get_object_or_404(db.weather.find(), _id=pk)

            # Retorna o documento encontrado no contexto do template
            return render(request, self.template_name, {'weather': weather_record})

        except Exception as e:
            # Em caso de erro, retorna uma resposta de erro ou redireciona para uma página de erro
            return redirect('error-page')  # Substitua 'error-page' pelo nome da sua página de erro

    def post(self, request, pk):  
        try:
            # Conecta-se ao MongoDB
            connection_string = "mongodb+srv://gkrcido:128Acido@cluster0.xglpozx.mongodb.net/"
            database_name = 'weather_rafaelRodrigues'
            client = MongoClient(connection_string)
            db = client[database_name]

            # Verifica se o objeto existe
            get_object_or_404(db.weather.find(), _id=pk)

            # Atualiza os campos do documento com os dados do formulário
            update_data = {
                "city": request.POST.get('city'),
                "date": datetime.strptime(request.POST.get('date'), '%Y-%m-%d'),  # Convert date string to datetime object
                "temperature": float(request.POST.get('temperature')),
                "pressure": float(request.POST.get('pressure')),
                "humidity": float(request.POST.get('humidity')),
                "precipitation": float(request.POST.get('precipitation')),
                "weather_condition": request.POST.get('weather_condition')
            }

            # Atualiza o documento no banco de dados
            db.weather.update_one({"_id": pk}, {"$set": update_data})

            # Redireciona o usuário para a página de listagem
            return redirect('weather-list')

        except Exception as e:
            # Em caso de erro, retorna uma resposta de erro ou redireciona para uma página de erro
            return redirect('error-page')  # Substitua 'error-page' pelo nome da sua página de erro
