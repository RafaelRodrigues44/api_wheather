from django.urls import path
from ..view.weatherCreateView import WeatherCreateView
from ..view.weatherListView import WeatherListView
from ..view.renderView import home

url_patterns = [
    path('', home, name='home'),
    path('weather/', WeatherListView.as_view(), name='weather-list'),
    path('weather/create/', WeatherCreateView.as_view(), name='weather-create'),
]


