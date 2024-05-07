import os
import jwt
import logging
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate 
from django.views import View
from django.contrib.auth.hashers import make_password
from user.repositories.repository import UserRepository
from rest_framework_simplejwt.tokens import RefreshToken
from uuid import uuid4
 
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
 
            existing_user = user_repo.get_user_by_email(email=email)
            if existing_user:
                raise ValueError('Este email já está em uso. Por favor, escolha outro.')
 
            hashed_password = make_password(password)
 
            new_user_data = {
                'uuid': str(uuid4()),
                'email': email,
                'username': username,
                'password': hashed_password,
            }
            user_repo.create_user(new_user_data)
 
            return render(request, 'base.html')
        except Exception as e:
            logger.error(f'Erro ao registrar usuário: {e}')
            return render(request, 'base.html')
 
class UserLogin(View):
    def get(self, request):
        return render(request, 'login.html')
 
    def post(self, request):
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
 
            # Chame a função authenticate para autenticar o usuário
            user = authenticate(request, username=email, password=password)
 
            if user is not None:
                # Autenticação bem-sucedida, gerando tokens
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
 
                # Logging do login bem-sucedido
                logger.info(f'Usuário {user.username} fez login com sucesso.')
 
                return render(request, 'main.html')
            else:
                raise ValueError('Credenciais inválidas. Por favor, tente novamente.')
        except Exception as e:
            logger.error(f'Erro ao fazer login: {e}')
            return redirect('login')