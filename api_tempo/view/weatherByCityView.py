from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET
from api_tempo.models.weatherRepositories import WeatherRepository

@require_GET
def get_weather_by_city(request, city):
    weather_repository = WeatherRepository()
    weather_documents = weather_repository.get_by_city(city)

    if weather_documents:
        # Convertendo IDs ObjectId para string
        for doc in weather_documents:
            doc['_id'] = str(doc['_id'])

        return render(request, 'weather_city.html', {'weather_list': weather_documents, 'city': city})
    else:
        return JsonResponse({"error": f"No weather data found for city '{city}'"}, status=404)
