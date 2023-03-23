from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('api/', include('chirpsounder.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
