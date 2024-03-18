from django.shortcuts import redirect
from api_tempo.models.customUsers import CustomUserManager
from django.http import HttpResponseNotFound
from django.views import View

class CustomUserDeleteView(View):
    def get(self, request, pk):
        # Inicialize o CustomUserManager
        user_manager = CustomUserManager()

        # Verifique se o usuário existe no MongoDB
        if user_manager.user_exists(pk):
            # Se o usuário existe, exclua-o
            user_manager.delete_user(pk)
        else:
            # Se o usuário não existir, retorne uma resposta de página não encontrada (404)
            return HttpResponseNotFound("Usuário não encontrado.")
        
        # Após excluir o usuário, redirecione para a lista de usuários (ou qualquer outra URL desejada)
        return redirect('customuser-list')
