import hashlib
from pyexpat.errors import messages
from urllib import response
from django.urls import reverse
import logging
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import make_password
from user.repositories.repository import UserRepository
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from uuid import uuid4
from django.contrib import messages
 
# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()  
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)  
 
class UserRegister(View):
    def get(self, request):
        return render(request, 'user_create.html')
 
    def post(self, request):
        try:
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
 
            user_repo = UserRepository()
 
            # Validação do email
            if not email or '@' not in email or '.' not in email:
                raise ValueError('Por favor, insira um email válido.')
 
            existing_user = user_repo.get_by_email(email=email)
            if existing_user:
                raise ValueError('Este email já está em uso. Por favor, escolha outro.')
 
            # Gerar o hash da senha 
            hashed_password = make_password(password)
 
            new_user_data = {
                'uuid': str(uuid4()),
                'email': email,
                'username': username,
                'password': hashed_password,
            }
            user_repo.create_user(new_user_data)
 
            return HttpResponseRedirect(reverse('user-list'))
        except Exception as e:
            logger.error(f'Erro ao registrar usuário: {e}')
            return render(request, 'base.html')
        

class UserList(View):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: HttpRequest):
        try:
            # Obtenha a lista de usuários do repositório
            users = UserRepository().get_all_users()

            # Converta o ObjectId para string se necessário
            for user in users:
                user['id'] = str(user['_id'])

            return render(request, "user_list.html", {"weather_records": users})

        except Exception as e:
            return HttpResponse(content="Erro ao obter os dados dos usuários.", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserListField(View):
    def get(self, request, **kwargs):
        email = kwargs.get('email')

        # Instancia o repositório do clima
        repository = UserRepository()

        try:
            # Busca os registros do clima para a cidade especificada
            if email:
                user_data = repository.get_by_email(email=email)
            else:
                user_data = repository.get_by_email()

            # Adiciona o campo 'id' aos objetos retornados
            for item in user_data:
                item['id'] = str(item['_id'])

            # Renderiza o template weather-list.html com os dados serializados
            return render(request, 'user_field.html', {'user_records': user_data})
        
        except Exception as e:
            return response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserDelete(View):
     def get(self, request, pk):
        repository = UserRepository()
        try:
            repository.delete(pk)
            return HttpResponseRedirect(reverse('user-list'))
        except Exception as e:
            return HttpResponseBadRequest(f"Erro ao excluir registro: {str(e)}")
        

class UserGetView(View):
    def get(self, request, pk):
        repository = UserRepository()
        try:
            user_data = repository.get(pk)
            if user_data:
                return render(request, 'user_update.html', {'user': user_data, 'pk': pk})  
            else:
                return HttpResponseBadRequest(f"Registro não encontrado para o ID: {pk}")
        except Exception as e:
            return HttpResponseBadRequest(f"Erro ao recuperar registro: {str(e)}")


class WeatherUpdateView(View):
    def post(self, request, pk):

        repository = UserRepository()

        try:
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
 
            user_repo = UserRepository()
 
            # Validação do email
            if not email or '@' not in email or '.' not in email:
                raise ValueError('Por favor, insira um email válido.')
 
            existing_user = user_repo.get_by_email(email=email)
            if existing_user:
                raise ValueError('Este email já está em uso. Por favor, escolha outro.')
 
            hashed_password = make_password(password)
 
            new_user_data = {
                'uuid': str(uuid4()),
                'email': email,
                'username': username,
                'password': hashed_password,
            }

                # Atualizar no MongoDB
            repository.update(pk, new_user_data)

            return HttpResponseRedirect(reverse('user-list'))
        except Exception as e:
            return HttpResponseBadRequest(f"Erro ao atualizar registro: {str(e)}")

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Autenticar o usuário
        user_repo = UserRepository()
        user = user_repo.authenticate_user(email, password)

        if user:
            # Autenticação bem-sucedida, redirecione para alguma página
            return redirect('weather-list')
        else:
            # Autenticação falhou
            print('A autenticação falhou')
            messages.error(request, 'Email ou senha incorretos.')

        return render(request, 'login.html')
    

class UserUpdate(View):
    pass