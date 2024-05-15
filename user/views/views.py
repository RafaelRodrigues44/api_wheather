from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.hashers import make_password
from user.repositories.repository import UserRepository
from user.models.userEntity import UserEntity
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect, render
from pyexpat.errors import messages
from django.urls import reverse
from django.views import View
from urllib import response
from rest_framework import status
from django.contrib import messages
from django.conf import settings
from uuid import uuid4
from datetime import datetime, timedelta
from django.contrib.auth import logout
import jwt



from django.utils.deprecation import MiddlewareMixin

  
 
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

        # Autentica o usuário
        user_repo = UserRepository()
        user = user_repo.authenticate_user(email, password)

        if user:
            # Autenticação bem-sucedida, gerar token e redirecionar para a página 'home'
            token = TokenManager.generate_token(user)
            response = redirect('home')  
            response = set_token_cookie(response, token)
            print(f'Token = {token}')
            print('Login feito com sucesso')
            return response
        else:
            # Autenticação falhou
            print('A autenticação falhou')
            messages.error(request, 'Email ou senha incorretos.')
            return render(request, 'login.html')

def set_token_cookie(response, token):
    # Define o token no cookie
    response.set_cookie('jwt_token', token, secure=True, httponly=True, samesite='Strict')
    # Retorna a resposta HTTP com o cookie definido
    return response


def get_user_from_token(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        # Cria um objeto de usuário com base nos dados do payload
        user = UserEntity(email=payload['email']) 
        return user
    except jwt.ExpiredSignatureError:
        return None  # Token expirado
    except jwt.InvalidTokenError:
        return None  # Token inválido

class TokenManager:
    @staticmethod
    def generate_token(user_data):
        payload = {
            'email': user_data.get('email'),  
            'exp': datetime.utcnow() + timedelta(minutes=5)  
        }
        return jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm='HS256')

    @staticmethod
    def refresh_token(token):
        payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
        # Verificar se o token está expirado e retornar um novo token com uma nova expiração
        if datetime.utcnow() > datetime.fromtimestamp(payload['exp']):
            user = UserEntity(username=payload['username'])  # Recupera o usuário do payload
            return TokenManager.generate_token(user)
        return None

    @staticmethod
    def verify_token(token):
        try:
            payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return None  # Token expirado
        except jwt.InvalidTokenError:
            return None  # Token inválido

    @staticmethod
    def get_authenticated_user(token):
        payload = TokenManager.verify_token(token)
        if payload:
            # Se o token for válido, retorne um objeto de usuário autenticado
            return UserEntity(username=payload['email'])
        return None

class LogoutView(View):
    def get(self, request):
        # Limpar a sessão do usuário
        logout(request)
        # Redirecionar para a página de login, por exemplo
        return redirect('login')
    
class UserUpdate(View):
    pass
