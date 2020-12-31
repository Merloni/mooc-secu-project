from django.db import models

from django.contrib.auth.models import User


class Account(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Message(models.Model):
    text = models.CharField(max_length=160)
