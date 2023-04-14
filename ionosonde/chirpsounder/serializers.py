from rest_framework import serializers
from djoser.serializers import UserSerializer
from django.db.models import Q

from .models import ConfigSettings, Swtracks, ScheduleSettings
from users.models import CustomUser


class CustomUserSerializer(UserSerializer):

    class Meta:
        model = CustomUser
        fields = ('email', 'id', 'first_name',
                  'last_name', 'is_staff')


class ConfigSettingsSerializer(serializers.ModelSerializer):

    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = ConfigSettings
        fields = ('programm_path', 'programm_config_path',
                  'storage_path', 'sample_rate', 'filter',
                  'filter_band', 'sample_count', 'decimation',
                  'fft_size', 'author')


class SwtracksSerializer(serializers.ModelSerializer):

    schedule = serializers.StringRelatedField(many=True, read_only=True)
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Swtracks
        fields = ('name', 'receive_station', 'transmit_station',
                  'repetition_period', 'chirptime', 'adjust_speed',
                  'session_duration', 'heterodyne_frequency',
                  'latitude', 'longitude', 'timestamp', 'author',
                  'schedule')


class ScheduleSettingsSerializer(serializers.ModelSerializer):

    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = ScheduleSettings
        fields = ('name', 'start_date_time', 'stop_date_time',
                  'swtrack', 'author')

    def validate(self, data):
        """
        Check for overlapping sessions and that start is before stop.
        """
        if self.instance:
            start_date_time = data.get(
                'start_date_time',
                self.instance.start_date_time,
            )
            stop_date_time = data.get(
                'stop_date_time',
                self.instance.stop_date_time
            )
        else:
            start_date_time = data.get('start_date_time')
            stop_date_time = data.get('stop_date_time')
        if start_date_time > stop_date_time:
            raise serializers.ValidationError('Stop must occur after start')
        overlapping_sessions = ScheduleSettings.objects.exclude(
            id=self.instance.id if self.instance else None).filter(
            Q(start_date_time__range=(start_date_time,
                                      stop_date_time)) |
            Q(stop_date_time__range=(start_date_time,
                                     stop_date_time)) |
            Q(start_date_time__lte=start_date_time,
              stop_date_time__gte=stop_date_time)
        )
        if overlapping_sessions.exists():
            raise serializers.ValidationError("You can't start or finish "
                                              "a session within another "
                                              "session being run.")
        return data
