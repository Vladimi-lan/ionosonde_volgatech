from rest_framework import viewsets

from .models import ConfigSettings, Swtracks, ScheduleSettings
from .serializers import (ConfigSettingsSerializer, SwtracksSerializer,
                          ScheduleSettingsSerializer)
from .permissions import IsOwnerOrReadOnly


class ConfigViewSet(viewsets.ModelViewSet):
    queryset = ConfigSettings.objects.all()
    serializer_class = ConfigSettingsSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user, partial=True)


class SwtracksViewSet(viewsets.ModelViewSet):
    queryset = Swtracks.objects.all()
    serializer_class = SwtracksSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user, partial=True)


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = ScheduleSettings.objects.all()
    serializer_class = ScheduleSettingsSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user, partial=True)
