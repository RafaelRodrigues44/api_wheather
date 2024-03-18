from django.shortcuts import redirect, render
from django.views import View
from api_tempo.models.customUsers import CustomUserManager

class CustomUserById(View):
    template_name = 'user_id.html'

    def get(self, request, pk=None):
        if pk is not None:
            # Chama a função get_id() para buscar o usuário pelo ID fornecido
            return self.get_id(request, pk)
        else:
            # Renderiza o formulário de busca se nenhum ID foi fornecido
            return render(request, self.template_name)

    def post(self, request):
        # Obtém o ID fornecido pelo usuário no formulário
        pk = request.POST.get('user_id')
        
        # Redireciona para a mesma view com o ID do usuário na URL
        return redirect('customuser-id', pk=pk)

    def get_id(self, request, pk):
        try:
            # Chama o método get_user_by_id do CustomUserManager para buscar o usuário pelo ID
            user_manager = CustomUserManager()
            user = user_manager.get_user_by_id(pk)
            
            if user:
                return render(request, self.template_name, {'user': user})
            else:
                # Retorna um erro 404 se o usuário não for encontrado
                return render(request, '404.html', status=404)
        except Exception as e:
            # Retorna um erro genérico se ocorrer um erro inesperado
            return render(request, '500.html', status=500)
