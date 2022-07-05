from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


# User = get_user_model()
class CustomUser(AbstractUser):
    """Абстрактная модель хранения пользовательских данных."""

    username = models.CharField(max_length=30, unique=True, help_text='login')
    email = models.EmailField(null=False, unique=True, help_text='email')
    first_name = models.CharField(max_length=30, help_text='Имя')
    last_name = models.CharField(max_length=30, help_text='Фамилия')
    sir_name = models.CharField(max_length=30, null=True, help_text='Отчество')
    is_active = models.BooleanField(default=True, help_text='Является ли пользователь активным')
    avatar = models.FileField(upload_to='storage/avatars/', default=None, null=True, help_text='Аватар')
    birthday = models.DateField(null=True, help_text='День рождения')
    agreement = models.DateTimeField(null=True, help_text='Пользовательское соглашение')
    created_at = models.DateTimeField(auto_now_add=True, help_text='Дата добавления')
    # logentry_set = models.CharField(max_length=30, unique=True, help_text='logentry_set')

    USERNAME_FIELD = "username"   # Имя, которое используем в качестве идентификатора


class Artist(models.Model):
    name = models.CharField(max_length=20)


class Album(models.Model):
    name = models.CharField(max_length=20)
    release_date = models.DateTimeField()
    artist = models.ForeignKey("Artist", related_name="albums", on_delete=models.CASCADE)


class Song(models.Model):
    name = models.CharField(max_length=20)
    duration = models.DecimalField(decimal_places=10, max_digits=10)
    album = models.ForeignKey("Album", related_name="songs", on_delete=models.CASCADE)
