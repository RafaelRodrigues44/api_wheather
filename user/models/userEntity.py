import uuid
import jwt
from core import settings 
from datetime import datetime, timedelta
from django.db import models
 
class UserEntity(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
 
    def __str__(self):
        return self.username
    
    @staticmethod
    def is_authenticated(self, token):
        try:
            # Decodificando o token
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

            # Verificando se o token está expirado
            if payload['exp'] < datetime.now:
                return False

            # Verificando se o email do token corresponde ao email do usuário
            user_email = payload.get('email')
            if user_email != self.email:
                return False

            return True
        except jwt.ExpiredSignatureError:
            # Token expirado
            return False
        except jwt.InvalidTokenError:
            # Token inválido
            return False