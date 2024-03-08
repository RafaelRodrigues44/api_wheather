from django.contrib import admin
from django.urls import path, include
from api_tempo.urls.urls import urls_patterns as api_tempo_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_tempo/', include(api_tempo_urls)),
]
