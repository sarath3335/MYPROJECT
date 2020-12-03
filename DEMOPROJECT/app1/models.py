from django.contrib.auth.models import AbstractUser
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    # type = models.CharField(max_length=100)

# Create your models here.
# class person(models.Model):
#     name = models.CharField(max_lenth=20)
#     country=models.CharField(max_length=35)
#     email=models.EmailField(max_length=254)
