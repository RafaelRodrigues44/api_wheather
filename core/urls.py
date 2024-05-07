from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from user.views.views import UserRegister
from api_tempo.urls.urls import url_patterns as api_tempo_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html'), name='home'), 
    path('api_tempo/', include(api_tempo_urls)), 
    path('api_tempo/user/create/', UserRegister.as_view(), name='user-create')
]