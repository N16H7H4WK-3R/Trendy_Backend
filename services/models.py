from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50, default='INDIA')
    phone_number = models.CharField(
        max_length=12, default='', null=False, blank=False)

    def __str__(self):
        return f'{self.username} - {self.id}'
