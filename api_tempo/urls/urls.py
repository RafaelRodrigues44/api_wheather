from django.urls import path
from ..view.weatherCreateView import WeatherInsert
#from ..view.weatherUpdateView import WeatherUpdateView
from ..view.weatherListView import WeatherView
from ..view.weatherDeleteView import WeatherDeleteView
from ..view.weatherFindFieldView import FindCityView
from ..view.renderView import home

url_patterns = [
    path('', home, name='home'),
    path('weather/', WeatherView.as_view(), name='weather-list'),
    path('weather/create/', WeatherInsert.as_view(), name='weather-create'),
    #path('weather/<int:pk>/update/', WeatherUpdateView.as_view(), name='weather-update'),
    path('weather/delete/<str:pk>', WeatherDeleteView.as_view(), name='weather-delete'),
    path('weather/city/<str:city>/', FindCityView.as_view(), name='weather-city'),
]


