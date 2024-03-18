from django.views import View
from rest_framework import status
from rest_framework.response import Response
from api_tempo.serializers.weatherSerializer import WeatherSerializer
from django.shortcuts import redirect, render
from api_tempo.models.weatherCollections import WeatherCollection 

class WeatherCreateViewSet(View):
    serializer_class = WeatherSerializer

    def get(self, request):
        return render(request, 'weather_create.html')

    def post(self, request):  # Alterado de create para post
        try:
            # Extrai os dados do corpo da solicitação
            data = request.data

            # Valida os dados usando o serializador
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)

            # Insere o novo registro usando a coleção WeatherCollection
            weather_collection = WeatherCollection()
            weather_collection.insert(serializer.validated_data)

            # Retorna uma resposta de sucesso
            return redirect('weather-list')

        except Exception as e:
            # Em caso de erro, retorna uma resposta de erro
            return Response({'detail': 'Erro ao criar o registro de clima.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
