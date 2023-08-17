from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


NULLABLE = {'blank': True, 'null': True}

class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')
    STUDENT = 'student', _('student')



class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=12, **NULLABLE, verbose_name='phone')
    city = models.CharField(max_length=30, **NULLABLE, verbose_name='city')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='аватар')
    is_active = models.BooleanField(default=True, verbose_name='пользователь верифицирован')
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.STUDENT, verbose_name='роль')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []