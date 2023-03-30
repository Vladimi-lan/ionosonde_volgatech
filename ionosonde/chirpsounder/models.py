from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model
from django.db import models

from users.models import CustomUser


# class SingletonModel(models.Model):
#     class Meta:
#         abstract = True
 
#     def save(self, *args, **kwargs):
#         self.__class__.objects.exclude(id=self.id).delete()
#         super(SingletonModel, self).save(*args, **kwargs)
 
#     @classmethod
#     def load(cls):
#         try:
#             return cls.objects.get()
#         except cls.DoesNotExist:
#             return cls()


class ConfigSettings(models.Model): 
    programm_path = models.CharField(
        verbose_name='путь до программы chirp.py',
        max_length=60,
        validators=[
            MinLengthValidator(
                2,
                message='Убедитесь, что длина пути более 2 символов'
            )
        ],
        help_text='путь до программы'
    )
    programm_config_path = models.CharField(
        verbose_name='путь до файла настроек',
        max_length=60,
        validators=[
            MinLengthValidator(
                2,
                message='Убедитесь, что длина пути более 2 символов'
            )
        ]
    )
    storage_path = models.CharField(
        verbose_name='путь записи ионограмм',
        max_length=60,
        validators=[
            MinLengthValidator(
                2,
                message='Убедитесь, что длина пути более 2 символов'
            )
        ]
    )
    sample_rate = models.IntegerField()
    filter = models.BooleanField()
    filter_band = models.IntegerField()
    sample_count = models.IntegerField()
    decimation = models.IntegerField()
    fft_size = models.IntegerField()
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='recent_author',
        verbose_name='Последний создатель файла настроек',
        help_text='Последний создатель файла настроек'
    )


class Swtracks(models.Model):

    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='swtracks',
        verbose_name='Автор'
    )
    name = models.CharField(
        verbose_name='Конфигурация трассы для зондирования.',
        max_length=120,
    )
    receive_station = models.CharField(
        verbose_name='Название приёмной станции',
        max_length=60,
        validators=[
            MinLengthValidator(
                2,
                message='Убедитесь, что длина названия содержит хотя бы 2 символа.'
            )
        ]
    )
    transmit_station = models.CharField(
        verbose_name='Название передающей станции',
        max_length=60,
        validators=[
            MinLengthValidator(
                2,
                message='Убедитесь, что длина названия содержит хотя бы 2 символа.'
            )
        ]
    )
    repetition_period = models.IntegerField(
        verbose_name='Период повторения сеанса зондирования.',
    )
    chirptime = models.IntegerField(
        verbose_name='Время начала синтеза ЛЧМ сигнала с 0 МГц.'
    )
    adjust_speed = models.IntegerField(
        verbose_name='Корректировка скорости ЛЧМ.'
    )
    session_duration = models.IntegerField(
        verbose_name='Длительность сеанса.'
    )
    heterodyne_frequency = models.IntegerField(
        verbose_name='Частота гетеродина.'
    )
    latitude = models.DecimalField(
        verbose_name='Широта.',
        max_digits=4,
        decimal_places=2,
    )
    longitude = models.DecimalField(
        verbose_name='Долгота.',
        max_digits=4,
        decimal_places=2,
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.name


class ScheduleSettings(models.Model):

    name = models.CharField(
        verbose_name='Название расписания',
        max_length=60,
        validators=[
            MinLengthValidator(
                1,
                message='Убедитесь, в названии есть хотя бы 1 символ'
            )
        ]
    )
    start_date_time = models.DateTimeField()
    stop_date_time = models.DateTimeField()
    swtrack = models.ForeignKey(
        Swtracks,
        on_delete=models.CASCADE,
        related_name='schedule'
    )
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='schedule',
        verbose_name='Создатель расписания',
        help_text='Создатель расписания'
    )

    def __str__(self) -> str:
        return self.name
