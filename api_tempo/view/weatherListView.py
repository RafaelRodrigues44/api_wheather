from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from bson import ObjectId  
from api_tempo.repositories import WeatherRepository
from api_tempo.serializers.weatherSerializer import WeatherSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class WeatherView(View):
    def get(self, request: HttpRequest):
        try:
            # A autenticação acontece automaticamente com JWTAuthentication
            weathers = list(WeatherRepository(collectionName='weathers').getAll())

            # Convertendo o ObjectId para string
            for item in weathers:
                item['id'] = str(item['_id'])

            serializer = WeatherSerializer(data=weathers, many=True)

            if serializer.is_valid():
                print(f'O valor da requisição é : {request}')
                return render(request, "weather_list.html", {"weather_records": serializer.data})
            else:
                return render(request, "weather_list.html", {"weather_records": []})

        except Exception as e:
            return HttpResponse(content="Erro ao obter os dados do clima.", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
