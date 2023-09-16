from django.db import models

class Login(models.Model):
    Email = models.CharField(max_length=100)
    Password = models.IntegerField()