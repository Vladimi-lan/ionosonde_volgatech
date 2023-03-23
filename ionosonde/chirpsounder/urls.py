from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (ConfigViewSet, ScheduleViewSet, SwtracksViewSet)


app_name = 'chirpsounder'

router = DefaultRouter()

router.register('config', ConfigViewSet)
router.register('swtracks', SwtracksViewSet)
router.register('schedule', ScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
