# Seting up custom user model to avioid problems with it later

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
