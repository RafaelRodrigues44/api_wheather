from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_tempo.models import CustomUser

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            if request.method == 'POST':
                email = request.data.get('email')
                password = request.data.get('password')

                if not email or not password:
                    return Response({'detail': 'Forneça email e senha.'}, status=status.HTTP_400_BAD_REQUEST)

                # Busca o usuário no banco de dados
                user = CustomUser.objects.filter(email=email).first()

                if user is not None and user.check_password(password):
                    # Autentica o usuário
                    login(request, user)
                    return Response({'detail': 'Login bem-sucedido'})
                else:
                    return Response({'detail': 'Erro no login. Verifique os dados e tente novamente.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'detail': 'Método não permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        except Exception as e:
            # Log the exception for debugging purposes
            print(f"Exception during login: {str(e)}")
            return Response({'detail': 'Erro interno no servidor'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
