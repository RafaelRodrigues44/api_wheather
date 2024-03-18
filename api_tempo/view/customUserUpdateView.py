from django.shortcuts import redirect, render
from api_tempo.models.customUsers import CustomUserManager
from django.http import HttpResponseNotFound
from django.views import View

class CustomUserUpdateView(View):
    template_name = 'user_edit.html'

    def get(self, request, pk):
        # Inicialize o CustomUserManager
        user_manager = CustomUserManager()

        # Obtenha o usuário do MongoDB com base no ID fornecido
        user = user_manager.get_user_by_id(pk)

        if user:
            # Renderize o formulário com os dados do usuário
            return render(request, self.template_name, {'user': user})
        else:
            # Se o usuário não existir, retorne uma resposta de página não encontrada (404)
            return HttpResponseNotFound("Usuário não encontrado.")

    def post(self, request, pk):
        # Inicialize o CustomUserManager
        user_manager = CustomUserManager()

        # Obtenha o usuário do MongoDB com base no ID fornecido
        user = user_manager.get_user_by_id(pk)

        if user:
            # Atualize os campos do usuário com os dados do formulário
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.email = request.POST.get("email")
            if request.POST.get("password"):
                user.set_password(request.POST.get("password"))

            # Atualize o usuário no MongoDB
            user_manager.update_user(pk, user)
        else:
            # Se o usuário não existir, retorne uma resposta de página não encontrada (404)
            return HttpResponseNotFound("Usuário não encontrado.")

        # Redirecione o usuário para a página de listagem
        return redirect('customuser-list')
