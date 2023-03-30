from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(
            self,
            username: str,
            first_name: str,
            last_name: str,
            email: str,
            password: str,
            is_staff=False,
            is_superuser=False):
        if not email:
            raise ValueError('User must have an email.')
        if not first_name:
            raise ValueError('User must have a first name.')
        if not last_name:
            raise ValueError('User must have a last name.')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        return user

    def create_superuser(
            self, username: str, first_name: str, last_name: str, email: str,
            password: str):
        user = self.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
        )
        user.save()
        return user


class CustomUser(AbstractUser):
    username = models.CharField(
        verbose_name='Login',
        max_length=150,
        unique=True
    )
    email = models.EmailField(
        verbose_name='Email',
        max_length=254,
        unique=True
    )
    first_name = models.CharField(
        verbose_name='First Name',
        max_length=255
    )
    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=255
    )

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
