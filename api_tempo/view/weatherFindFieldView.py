from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from api_tempo.repositories import WeatherRepository
from api_tempo.serializers.weatherSerializer import WeatherSerializer

class FindCityView(APIView):
    def get(self, request, **kwargs):
        city = kwargs.get('city')

        # Instancia o repositório do clima
        repository = WeatherRepository(collectionName='weathers')

        try:
            # Busca os registros do clima para a cidade especificada
            if city:
                weather_data = repository.getAll(city=city)
            else:
                weather_data = repository.getAll()

            # Serializa os dados do clima
            serializer = WeatherSerializer(weather_data, many=True)

            # Renderiza o template weather-list.html com os dados serializados
            return render(request, 'weather_field.html', {'weather_records': serializer.data})
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

   