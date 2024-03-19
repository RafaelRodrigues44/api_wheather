from django.urls import path
from ..view.customUserView import CustomUserViewSet
from ..view.customCreateUserview import CustomCreateUserView
from ..view.customUserUpdateView import CustomUserUpdateView
from ..view.customUserDeleteview import CustomUserDeleteView
from ..view.customUserById import CustomUserById
from ..view.weatherCreateView import WeatherCreateViewSet
from ..view.weatherUpdateView import WeatherUpdateView
from ..view.weatherListView import WeatherListView
from ..view.weatherDeleteView import WeatherDeleteView
from ..view.weatherFindbyCity import WeatherFindByCity
from ..view.loginview import LoginView
from ..view.renderView import home

url_patterns = [
    path('', home, name='home'),
    path('users/create/', CustomCreateUserView.as_view({'post': 'create', 'get': 'show_create_form'}), name='customuser-create'),
    path('users/', CustomUserViewSet.as_view({'get': 'list'}), name='customuser-list'),
    path('users/<int:pk>/update/', CustomUserUpdateView.as_view(), name='customuser-update'),
    path('users/<int:pk>/delete/', CustomUserDeleteView.as_view(), name='customuser-delete'),
    path('users/search/', CustomUserById.as_view(), name='customuser-id-form'),
    path('users/search/<int:pk>/', CustomUserById.as_view(), name='customuser-id'),
    path('weather/', WeatherListView.as_view({'get': 'list'}), name='weather-list'),
    path('weather/create/', WeatherCreateViewSet.as_view({'post': 'create', 'get': 'show_create_form'}), name='weather-create'),
    path('weather/<int:pk>/', WeatherListView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('weather/<int:pk>/update/', WeatherUpdateView.as_view(), name='weather-update'),
    path('weather/<int:pk>/delete/', WeatherDeleteView.as_view(), name='weather-delete'),
    path('weather/<str:city>/city/', WeatherFindByCity.as_view(), name='weather-city'),
    
    path('login/', LoginView.as_view(), name='login')
]


