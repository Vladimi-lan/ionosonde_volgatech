from rest_framework import serializers
from djoser.serializers import UserSerializer

from .models import ConfigSettings, Swtracks, ScheduleSettings
from users.models import CustomUser


class CustomUserSerializer(UserSerializer):

    class Meta:
        model = CustomUser
        fields = ('email', 'id', 'first_name',
                  'last_name')


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

    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ScheduleSettings
        fields = ('name', 'start_date_time', 'stop_date_time',
                  'swtrack', 'owner')

    def validate(self, data):
        """
        Check that start is before stop and not within another session.
        """
        if data['start_date_time'] > data['stop_date_time']:
            raise serializers.ValidationError('Stop must occur after start')
        elif ScheduleSettings.objects.filter(
            start_date_time__lte=data['start_date_time'],
            stop_date_time__gte=data['start_date_time']
        ):
            raise serializers.ValidationError("You can't start a session "
                                              "within another session "
                                              "being run")
        return data
