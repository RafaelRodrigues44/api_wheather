from django.http import JsonResponse
from django.views.generic import View
from api_tempo.models.weatherRepositories import WeatherRepository  

class WeatherDeleteView(View):
    def post(self, request, *args, **kwargs):
        document_id = kwargs.get('document_id')  # Obtém o ID do documento da URL
        try:
            weather_obj = WeatherRepository.objects.get(pk=document_id)  # Obtém o objeto WeatherRepository pelo ID
            weather_obj.delete()  # Exclui o objeto
            return JsonResponse({'message': 'Objeto excluído com sucesso'}, status=200)
        except WeatherRepository.DoesNotExist:
            return JsonResponse({'error': 'Objeto não encontrado'}, status=404)
