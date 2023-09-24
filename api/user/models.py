from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)

    # Define unique related names for the group and permission relationships
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='Trendy_users'  # Change this related_name
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='Trendy_users_permissions'  # Change this related_name
    )
