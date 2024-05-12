from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from user.views.views import UserRegister
from user.views.views import UserList
from user.views.views import UserDelete
from user.views.views import UserListField
from user.views.views import UserUpdate
from user.views.views import UserGetView
from user.views.views import Login
from api_tempo.urls.urls import url_patterns as api_tempo_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html'), name='home'), 
    path('api_tempo/', include(api_tempo_urls)), 
    path('api_tempo/users/', UserList.as_view(), name='user-list'),
    path('api_tempo/user/create/', UserRegister.as_view(), name='user-create'),
    path('api_tempo/user/delete/<str:pk>/', UserDelete.as_view(), name='user-delete'),
    path('api_tempo/user/get/<str:username>/', UserListField.as_view(), name='user-field'),
    path('api_tempo/user/get/<str:pk>/', UserGetView.as_view(), name='user-get'),
    path('api_tempo/user/update/<str:pk>/', UserUpdate.as_view(), name='user-update'),
    path('api_tempo/login/', Login.as_view(), name='login'),
]