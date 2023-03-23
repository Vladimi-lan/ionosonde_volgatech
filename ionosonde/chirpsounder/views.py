from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ConfigSettings, Swtracks, ScheduleSettings
from .serializers import (ConfigSettingsSerializer, SwtracksSerializer,
                          ScheduleSettingsSerializer)


class ConfigViewSet(viewsets.ModelViewSet):
    queryset = ConfigSettings.objects.all()
    serializer_class = ConfigSettingsSerializer


class SwtracksViewSet(viewsets.ModelViewSet):
    queryset = Swtracks.objects.all()
    serializer_class = SwtracksSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = ScheduleSettings.objects.all()
    serializer_class = ScheduleSettingsSerializer
