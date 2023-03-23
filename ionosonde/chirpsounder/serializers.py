from rest_framework import serializers

from .models import ConfigSettings, Swtracks, ScheduleSettings


class ConfigSettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConfigSettings
        fields = ('programm_path', 'programm_config_path',
                  'storage_path', 'sample_rate', 'filter',
                  'filter_band', 'sample_count', 'decimation',
                  'fft_size', 'author')


class SwtracksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Swtracks
        fields = ('name', 'receive_station', 'transmit_station',
                  'repetition_period', 'chirptime', 'adjust_speed',
                  'session_duration', 'heterodyne_frequency',
                  'latitude', 'longitude', 'timestamp', 'author')


class ScheduleSettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScheduleSettings
        fields = ('name', 'start_date_time', 'stop_date_time',
                  'swtrack', 'owner')
