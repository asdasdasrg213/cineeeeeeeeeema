from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/avatars')
    favorite_movies = models.ManyToManyField('movie.Movie', related_name='selected_movies')
    