from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from user.views.views import UserRegister
from user.views.views import UserList
from user.views.views import UserDelete
from user.views.views import UserListField
from user.views.views import UserUpdateView
from user.views.views import UserGetView
from user.views.views import Login
from user.views.views import LogoutView
from api_tempo.view.aboutRender import About

from api_tempo.urls.urls import url_patterns as api_tempo_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html'), name='home'), 
    path('/about', About.as_view(), name='about'),
    path('api_tempo/', include(api_tempo_urls)), 
    path('api_tempo/users/', UserList.as_view(), name='user-list'),
    path('api_tempo/user/create/', UserRegister.as_view(), name='user-create'),
    path('api_tempo/user/delete/<str:pk>/', UserDelete.as_view(), name='user-delete'),
    path('api_tempo/user/get/<str:email>/', UserListField.as_view(), name='user-field'),
    path('api_tempo/user/<str:pk>/', UserGetView.as_view(), name='user-get'),
    path('api_tempo/user/update/<str:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('api_tempo/login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]