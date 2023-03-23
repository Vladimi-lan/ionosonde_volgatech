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


class APIConfig(APIView):
    def get(self, request):
        configs = get_list_or_404(ConfigSettings)
        serializer = ConfigSettingsSerializer(configs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ConfigSettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIConfigDetail(APIView):
    def get(self, request, pk):
        config = get_object_or_404(ConfigSettings, id=pk)
        serializer = ConfigSettingsSerializer(config)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        config = get_object_or_404(ConfigSettings, id=pk)
        serializer = ConfigSettingsSerializer(config, data=request.data,
                                              partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        config = get_object_or_404(ConfigSettings, id=pk)
        serializer = ConfigSettingsSerializer(config, data=request.data,
                                              partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        config = get_object_or_404(ConfigSettings, id=pk)
        config.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def api_swtracks(request):
    if request.method == 'POST':
        serializer = SwtracksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    swtracks_list = get_list_or_404(Swtracks)
    serializer = SwtracksSerializer(swtracks_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class SwtracksViewSet(viewsets.ModelViewSet):
    queryset = Swtracks.objects.all()
    serializer_class = SwtracksSerializer


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_swtracks_detail(request, pk):
    swtrack = get_object_or_404(Swtracks, id=pk)
    if request.method == 'PUT' or request.method == 'PATCH':
        serializer = SwtracksSerializer(swtrack, data=request.data,
                                        partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        swtrack.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = SwtracksSerializer(swtrack)
    return Response(serializer.data, status=status.HTTP_200_OK)


class ScheduleList(generics.ListCreateAPIView):
    queryset = get_list_or_404(ScheduleSettings)
    serializer_class = ScheduleSettingsSerializer


class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScheduleSettings.objects.all()
    serializer_class = ScheduleSettingsSerializer
