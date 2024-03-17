from pyexpat.errors import messages
from django.views import View
from django.http import JsonResponse
from api_tempo.models import CustomUser
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.contrib import messages

class CustomUserUpdateView(View):
    template_name = 'user_edit.html'

    def get(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        # Aqui você pode adicionar o código necessário para preencher o formulário com os dados do usuário
        return render(request, self.template_name, {'user': user})

    def post(self, request, pk):  # Alterado para post para lidar com o envio do formulário
        user = get_object_or_404(CustomUser, pk=pk)
        
        # Atualize os campos com os dados do formulário
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")
        
        if request.POST.get("password"):
            user.set_password(request.POST.get("password"))

        user.save()
        
        # Redireciona o usuário para página de listagem
        return redirect('customuser-list')
