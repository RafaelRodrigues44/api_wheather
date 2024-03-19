from django.shortcuts import render
from django.views import View
from api_tempo.models import Weather
from api_tempo.models.weatherRepositories import WeatherRepository

class WeatherCreateView(View):
    template_name = 'weather_create.html'
    repository = WeatherRepository()

    def get(self, request):
        # Renderize o formulário para inserção de dados
        return render(request, self.template_name)

    def post(self, request):
        # Obtenha os dados do formulário
        city = request.POST.get('city')
        date = request.POST.get('date')
        temperature = float(request.POST.get('temperature'))
        pressure = float(request.POST.get('pressure'))
        humidity = float(request.POST.get('humidity'))
        precipitation = float(request.POST.get('precipitation'))
        weather_condition = request.POST.get('weather_condition')

        # Crie um objeto Weather
        weather = Weather(
            city=city,
            date=date,
            temperature=temperature,
            pressure=pressure,
            humidity=humidity,
            precipitation=precipitation,
            weather_condition=weather_condition
        )

        # Insira o objeto no banco de dados
        self.repository.create(weather)

        # Renderize a página de sucesso ou redirecione para outra página
        return render(request, 'base.html')
