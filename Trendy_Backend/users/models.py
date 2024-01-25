from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser, PermissionsMixin):
    USER_TYPE_CHOICES = [
        ("admin", "Admin"),
        ("user", "Normal User"),
        ("employee", "Employee/Collaborative Business"),
    ]

    user_type = models.CharField(
        max_length=20, choices=USER_TYPE_CHOICES, default="user"
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
