 @action(detail=False, methods=['get'])
    def filter_by_city(self, request):
        city_name = request.query_params.get('city', None)
        
        if not city_name:
            return Response({'error': 'City name parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

        weather_forecasts = Weather.objects.filter(city__iexact=city_name)
        serializer = self.get_serializer(weather_forecasts, many=True)
        return Response(serializer.data)

  