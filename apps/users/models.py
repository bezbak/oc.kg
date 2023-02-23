from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class User(AbstractUser):
    profile_image = models.ImageField(
        upload_to='profile_image/',
        blank=True,
        null=True,
        default='https://cdn.vectorstock.com/i/preview-1x/66/14/default-avatar-photo-placeholder-profile-picture-vector-21806614.jpg'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    balance = models.PositiveBigIntegerField(
        verbose_name="Баланс пользователя",
        default = 0
    )
    wallet = models.CharField(
        default=uuid.uuid4,
        verbose_name="Кошелек",
        max_length=150,
        unique=True
    )

    def __str__(self):
        return  self.username

class WatchedMovie(models.Model):
    watched_movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE, related_name='watched_movie')
    watched_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watched_user')
    