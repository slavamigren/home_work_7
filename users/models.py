from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}

class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=12, **NULLABLE, verbose_name='phone')
    city = models.CharField(max_length=30, **NULLABLE, verbose_name='city')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='аватар')
    is_active = models.BooleanField(default=True, verbose_name='пользователь верифицирован')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []