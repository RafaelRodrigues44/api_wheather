from urllib import request
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from api_tempo.models import CustomUser

class CustomUserById(View):
    template_name = 'user_id.html'

    def get(self, request, pk=None):
        if pk is not None:
            # Se um ID de usuário foi fornecido na URL, chama a função get_id()
            return self.get_id(request, pk)
        else:
            # Caso contrário, renderiza o formulário de busca
            return render(request, self.template_name)

    def post(self, request):
        # Obtém o ID fornecido pelo usuário no formulário
        pk = request.POST.get('user_id')
        
        # Redireciona para a mesma view com o ID do usuário na URL
        return redirect('customuser-id', pk=pk)

    def get_id(self, request, pk):
        # Busca o usuário com base no ID fornecido
        user = get_object_or_404(CustomUser, pk=pk)
        
        # Retorna o usuário encontrado no contexto do template
        return render(request, self.template_name, {'user': user})

    
