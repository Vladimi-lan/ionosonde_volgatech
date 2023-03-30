# Generated by Django 4.1.3 on 2023-03-30 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chirpsounder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='swtracks',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='swtracks', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='schedulesettings',
            name='owner',
            field=models.ForeignKey(help_text='Создатель расписания', on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to=settings.AUTH_USER_MODEL, verbose_name='Создатель расписания'),
        ),
        migrations.AddField(
            model_name='schedulesettings',
            name='swtrack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='chirpsounder.swtracks'),
        ),
        migrations.AddField(
            model_name='configsettings',
            name='author',
            field=models.ForeignKey(help_text='Последний создатель файла настроек', on_delete=django.db.models.deletion.CASCADE, related_name='recent_author', to=settings.AUTH_USER_MODEL, verbose_name='Последний создатель файла настроек'),
        ),
    ]
