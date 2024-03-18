from rest_framework import serializers
from api_tempo.models.customUsers import CustomUser

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    is_active = serializers.BooleanField(default=True)
    is_staff = serializers.BooleanField(default=False)

    def create(self, validated_data):
        user_manager = CustomUser()
        user_manager.insert_user(validated_data)
        return validated_data

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.save()
        return instance
