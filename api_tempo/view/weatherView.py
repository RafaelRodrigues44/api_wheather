from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from api_tempo.models.weatherModel import Weather
from api_tempo.serializers.weatherSerializer import WeatherSerializer

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    @action(detail=False, methods=['get'])
    def list_cities(self, request):
        cities = Weather.objects.values_list('city', flat=True).distinct()
        return Response({'cities': cities})

    @action(detail=False, methods=['get'])
    def filter_by_city(self, request):
        city_name = request.query_params.get('city', None)
        
        if not city_name:
            return Response({'error': 'City name parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

        weather_forecasts = Weather.objects.filter(city__iexact=city_name)
        serializer = self.get_serializer(weather_forecasts, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def create_weather(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
