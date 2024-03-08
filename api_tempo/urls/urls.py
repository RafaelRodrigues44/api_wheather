from django.urls import path
from ..view.customUserView import CustomUserViewSet
from ..view.weatherView import WeatherViewSet
from ..view.loginview import LoginView

urls_patterns = [
    path('users/', CustomUserViewSet.as_view({'get': 'list', 'post': 'create'}), name='customuser-list-create'),
    path('users/<int:pk>/', CustomUserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='customuser-retrieve-update-destroy'),
    path('weather/', WeatherViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('weather/filter_by_city/', WeatherViewSet.as_view({'get': 'filter_by_city'}), name='weather-filter-by-city'),
    path('weather/<int:pk>/', WeatherViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('login/', LoginView.as_view(), name='login')
]


