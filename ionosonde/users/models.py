from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(
        verbose_name='Логин',
        max_length=150,
        unique=True
    )
    email = models.EmailField(
        verbose_name='Почта',
        max_length=254,
        unique=True
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=150
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=150
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.username
