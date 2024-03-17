# view.py
from django.shortcuts import render, redirect
from rest_framework import viewsets
from api_tempo.models import CustomUser
from api_tempo.serializers.customUserSerializer import CustomUserSerializer

class CustomCreateUserView(viewsets.ViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
    def show_create_form(self, request):
        # Se for uma solicitação GET, renderiza o formulário de criação de usuário
        serializer = self.serializer_class()
        return render(request, 'user_create.html', {'serializer': serializer})

    def create(self, request, *args, **kwargs):
        # Tenta criar um novo usuário com base nos dados enviados
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Redireciona para a página de lista de usuários após a criação bem-sucedida
            return redirect('customuser-list')
        # Se os dados não forem válidos, renderiza novamente o formulário de criação com os erros
        return self.show_create_form(request)