from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (api_config, api_config_detail,
                    api_schedule, api_schedule_detail,
                    api_swtracks, api_swtracks_detail)


app_name = 'chirpsounder'

# router = DefaultRouter()

# router.register()

urlpatterns = [
    path('config/', api_config),
    path('config/<int:pk>/', api_config_detail),
    path('schedule/', api_schedule),
    path('schedule/<int>:pk/', api_schedule_detail),
    path('swtracks/', api_swtracks),
    path('swtracks/<int>:pk/', api_swtracks_detail),
]
