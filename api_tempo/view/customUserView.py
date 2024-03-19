# views/customUserView.py
from rest_framework import status, viewsets
from rest_framework.response import Response
from api_tempo.models import CustomUser
from django.shortcuts import render

class CustomUserViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        return render(request, 'user_list.html', {'users': users})
    

