from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (APIConfig, APIConfigDetail,
                    ScheduleList, ScheduleDetail,
                    SwtracksViewSet)


app_name = 'chirpsounder'

router = DefaultRouter()

router.register('swtracks', SwtracksViewSet)

urlpatterns = [
    path('config/', APIConfig.as_view()),
    path('config/<int:pk>/', APIConfigDetail.as_view()),
    path('schedule/', ScheduleList.as_view()),
    path('schedule/<int:pk>/', ScheduleDetail.as_view()),
    path('', include(router.urls)),
]
