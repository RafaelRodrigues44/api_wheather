from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from api_tempo.models import Weather
from api_tempo.serializers.weatherSerializer import WeatherSerializer
from django.shortcuts import render, redirect

class WeatherCreateViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    def show_create_form(self, request):
        # Se for uma solicitação GET, renderiza o formulário de criação de usuário
        serializer = self.serializer_class()
        return render(request, 'weather_create.html', {'serializer': serializer})


    def create(self, request, *args, **kwargs):
        # Tenta criar um novo usuário com base nos dados enviados
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return redirect('weather-list')
        
        return self.show_create_form(request)
