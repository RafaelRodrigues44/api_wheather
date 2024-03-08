# views/customUserView.py
from rest_framework import status, viewsets
from rest_framework.response import Response
from api_tempo.models import CustomUser
from api_tempo.serializers.customUserSerializer import CustomUserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        instance = serializer.instance
        if "first_name" in self.request.data:
            instance.first_name = self.request.data["first_name"]
        if "last_name" in self.request.data:
            instance.last_name = self.request.data["last_name"]
        if "email" in self.request.data:
            instance.email = self.request.data["email"]
        if "password" in self.request.data:
            instance.set_password(self.request.data["password"])
        instance.save()

    def perform_destroy(self, instance):
        instance.delete()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
