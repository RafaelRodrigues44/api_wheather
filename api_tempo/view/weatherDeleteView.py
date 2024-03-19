# View WeatherDeleteView
from django.http import JsonResponse
from django.views.generic import View
from api_tempo.models.weatherRepositories import WeatherRepository  

class WeatherDeleteView(View):
    pass