from rest_framework import serializers

class WeatherSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=255, allow_blank=True)
    temperature = serializers.FloatField()
    date = serializers.DateTimeField()
    city = serializers.CharField(max_length=255, allow_blank=True)
    atmosphericPressure = serializers.FloatField(required=False)
    humidity = serializers.FloatField(required=False)
    weather = serializers.CharField(max_length=255, allow_blank=True)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Safely retrieve 'id' from instance or default to None
        representation['id'] = instance.get('id')
        
        # Format the date if available
        if 'date' in instance and instance['date']:
            # Convert datetime to the desired string format
            representation['date'] = instance['date'].strftime("%d/%m/%Y %H:%M:%S")
        else:
            representation['date'] = ''
        
        return representation
