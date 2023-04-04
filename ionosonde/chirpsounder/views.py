from rest_framework import viewsets

from .models import ConfigSettings, Swtracks, ScheduleSettings
from .serializers import (ConfigSettingsSerializer, SwtracksSerializer,
                          ScheduleSettingsSerializer)


class ConfigViewSet(viewsets.ModelViewSet):
    queryset = ConfigSettings.objects.all()
    serializer_class = ConfigSettingsSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class SwtracksViewSet(viewsets.ModelViewSet):
    queryset = Swtracks.objects.all()
    serializer_class = SwtracksSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = ScheduleSettings.objects.all()
    serializer_class = ScheduleSettingsSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
