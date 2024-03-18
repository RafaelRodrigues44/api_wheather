from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from api_tempo.models.customUsers import CustomUser
from api_tempo.models.userCollections import CustomUserManagerMongoDB

class CreateUserView(View):
    def post(self, request):
        # Obtenha os dados do corpo da solicitação
        data = request.POST

        # Verifique se o e-mail já está em uso
        if CustomUser.objects.filter(email=data['email']).exists():
            return JsonResponse({'error': 'Este e-mail já está em uso'}, status=400)

        # Crie o usuário no Django
        user = CustomUser.objects.create_user(
            email=data['email'],
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name']
        )

        # Salve o usuário no MongoDB
        user_manager_mongo = CustomUserManagerMongoDB()
        user_manager_mongo.insert_user({
            'email': data['email'],
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            # Adicione outros campos conforme necessário
        })

        # Autentique o usuário recém-criado
        user = authenticate(request, email=data['email'], password=data['password'])
        if user is not None:
            login(request, user)
            return JsonResponse({'success': 'Usuário criado e autenticado com sucesso'}, status=201)
        else:
            return JsonResponse({'error': 'Falha na autenticação'}, status=400)

    def get(self, request):
        return render(request, 'user_create.html')
