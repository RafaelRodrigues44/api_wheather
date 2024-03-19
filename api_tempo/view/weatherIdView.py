from django.http import JsonResponse
from django.views.decorators.http import require_GET
from api_tempo.models.weatherRepositories import WeatherRepository

@require_GET
def get_weather_by_id(request, document_id):
    weather_repository = WeatherRepository()
    weather_document = weather_repository.get_by_id(document_id)

    if weather_document:
        # Convertendo o ID ObjectId para string
        weather_document['_id'] = str(weather_document['_id'])
        return JsonResponse({"weather": weather_document}, status=200)
    else:
        return JsonResponse({"error": "Weather not found"}, status=404)
