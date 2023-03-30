from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (ConfigViewSet, ScheduleViewSet, SwtracksViewSet)
from users.views import CustomUserViewSet


app_name = 'chirpsounder'

router = DefaultRouter()

router.register(r'users', CustomUserViewSet, basename='users')
router.register('config', ConfigViewSet)
router.register('swtracks', SwtracksViewSet)
router.register('schedule', ScheduleViewSet)

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include(router.urls)),
]
