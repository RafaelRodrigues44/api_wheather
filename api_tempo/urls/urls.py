from django.urls import path
from ..view.weatherCreateView import WeatherCreateView
from ..view.weatherListView import WeatherListView
from ..view.weatherDeleteView import WeatherDeleteView
from ..view.weatherIdView import get_weather_by_id
from ..view.weatherByCityView import get_weather_by_city
from ..view.renderView import home

url_patterns = [
    path('', home, name='home'),
    path('weather/', WeatherListView.as_view(), name='weather-list'),
    path('weather/create/', WeatherCreateView.as_view(), name='weather-create'),
    path('weather/delete/<str:document_id>', WeatherDeleteView.as_view(), name='weather-delete'),
    path('weather/<str:document_id>/', get_weather_by_id, name='get_weather_by_id'),
    path('weather/city/<str:city>/', get_weather_by_city, name='get_weather_by_city'),
]


