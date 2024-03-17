from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from api_tempo.serializers.weatherSerializer import WeatherSerializer  
from api_tempo.models.weatherModel import Weather

class WeatherUpdateView(View):
    template_name = 'weather_edit.html'

    def get(self, request, pk):
        weather = get_object_or_404(Weather, pk=pk)
        # Here you can add the code necessary to fill the form with the user's data
        return render(request, self.template_name, {'weather': weather})

    def post(self, request, pk):  
        weather = get_object_or_404(Weather, pk=pk)
        # Update fields with the form data
        weather.city = request.POST.get('city')
        weather.date = request.POST.get('date')
        weather.temperature = request.POST.get('temperature')
        weather.pressure = request.POST.get('pressure')
        weather.humidity = request.POST.get('humidity')
        weather.precipitation = request.POST.get('precipitation')
        weather.weather_condition = request.POST.get('weather_condition')
        weather.save()
        # Redirect the user to the listing page
        return redirect('weather-list')
