from django.utils.deprecation import MiddlewareMixin
from .views.views import TokenManager

class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        token = request.COOKIES.get('jwt_token')
        if token:
            user = TokenManager.get_authenticated_user(token)
            if user:
                request.user = user
            else:
                request.user = None
        else:
            request.user = None
