from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api_tempo.models.weatherModel import Weather
from api_tempo.serializers.weatherSerializer import WeatherSerializer
from django.shortcuts import render

class WeatherListView(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    @action(detail=False, methods=['get'])
    def list_cities(self, request):
        cities = Weather.objects.values_list('city', flat=True).distinct()
        return Response({'cities': cities})

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        weather_records = serializer.data
        return render(request, 'weather_list.html', {'weather_records': weather_records})

   
   
