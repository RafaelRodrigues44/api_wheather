from django.shortcuts import render
from django.views import View
from api_tempo.models.weatherRepositories import WeatherRepository

class WeatherListView(View):
    template_name = 'weather_list.html'

    def get(self, request):
        weather_repo = WeatherRepository()
        weather_documents = weather_repo.get_all()
        return render(request, self.template_name, {'weather_collections': weather_documents})
