
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import get_object_or_404
from api_tempo.models import CustomUser

class CustomUserDeleteView(View):
    def get(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        user.delete()
        return redirect('customuser-list')
