from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ConfigSettings, Swtracks, ScheduleSettings
from .serializers import (ConfigSettingsSerializer, SwtracksSerializer,
                          ScheduleSettingsSerializer)



@api_view(['GET', 'POST'])
def api_config(request):
    if request.method == 'POST':
        serializer = ConfigSettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    configs = get_list_or_404(ConfigSettings)
    serializer = ConfigSettingsSerializer(configs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_config_detail(request, pk):
    config = get_object_or_404(ConfigSettings, id=pk)
    if request.method == 'PUT' or request.method == 'PATCH':
        serializer = ConfigSettingsSerializer(config, data=request.data,
                                              partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        config.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = ConfigSettingsSerializer(config)
    return Response(serializer.data, status=status.HTTP_200_OK)


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


@api_view(['GET', 'POST'])
def api_schedule(request):
    if request.method == 'POST':
        serializer = ScheduleSettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    schedule_list = get_list_or_404(ScheduleSettings)
    serializer = ScheduleSettingsSerializer(schedule_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_schedule_detail(request, pk):
    schedule = get_object_or_404(ScheduleSettings, id=pk)
    if request.method == 'PUT' or request.method == 'PATCH':
        serializer = ScheduleSettingsSerializer(schedule, data=request.data,
                                                partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = ScheduleSettingsSerializer(schedule)
    return Response(serializer.data, status=status.HTTP_200_OK)
