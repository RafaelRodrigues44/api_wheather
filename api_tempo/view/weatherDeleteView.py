from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from api_tempo.repositories import WeatherRepository

class WeatherDeleteView(View):
    def get(self, request, pk):
        repository = WeatherRepository(collectionName='weathers')
        try:
            repository.delete(pk)
            return HttpResponseRedirect(reverse('weather-list'))
        except Exception as e:
            return HttpResponseBadRequest(f"Erro ao excluir registro: {str(e)}")
