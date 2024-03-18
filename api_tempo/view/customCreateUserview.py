from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from api_tempo.models.customUsers import CustomUser
from api_tempo.models.userCollections import CustomUserManagerMongoDB

class CreateUserView(View):
    def post(self, request):
        # Obtenha os dados do corpo da solicitação
        data = request.POST

        # Crie o usuário no Django
        user = CustomUser.objects.create_user(
            email=data['email'],
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name']
        )

        if user:
            # Salve o usuário no MongoDB
            user_manager_mongo = CustomUserManagerMongoDB()
            user_manager_mongo.insert_user({
                'email': data['email'],
                'first_name': data['first_name'],
                'last_name': data['last_name'],
            })

            # Autentique o usuário recém-criado
            user = authenticate(request, email=data['email'], password=data['password'])
            if user is not None:
                login(request, user)
                return JsonResponse({'success': 'Usuário criado e autenticado com sucesso'}, status=201)

        return JsonResponse({'error': 'Falha ao criar o usuário'}, status=400)

    def get(self, request):
        return render(request, 'user_create.html')
