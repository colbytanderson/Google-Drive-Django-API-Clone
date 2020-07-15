from django.contrib.auth.models import (
   AbstractBaseUser, PermissionsMixin,
)
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=30, primary_key=True)
    USERNAME_FIELD = 'username'