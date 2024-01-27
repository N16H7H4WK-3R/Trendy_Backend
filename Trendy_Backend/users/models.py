from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group


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
        ("user", "User"),
        ("seller", "Seller"),
    ]

    user_type = models.CharField(
        max_length=20, choices=USER_TYPE_CHOICES, default="user"
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    groups = models.ManyToManyField(Group, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.user_type == "admin"

    @property
    def is_seller(self):
        return self.user_type == "seller"

    @property
    def is_user(self):
        return self.user_type == "user"

    def has_permission_to_view(self, obj):
        return self.is_authenticated and obj == self

    def has_permission_to_edit(self, obj):
        return self.has_permission_to_view(obj)

    def has_permission_to_delete(self, obj):
        return self.has_permission_to_view(obj)

    def has_permission_to_update(self, obj):
        return self.has_permission_to_view(obj)

    def has_seller_permission(self, obj):
        return self.is_authenticated and self.is_seller and obj == self

    def has_permission_to_view_sellers_data(self, obj):
        return self.is_authenticated and self.is_seller and obj == self

    def has_permission_to_edit_sellers_data(self, obj):
        return self.has_seller_permission(obj)

    def has_permission_to_delete_sellers_data(self, obj):
        return self.has_seller_permission(obj)

    def has_permission_to_update_sellers_data(self, obj):
        return self.has_seller_permission(obj)

    def has_admin_permission(self, obj):
        return self.is_authenticated and self.is_admin and obj == self

    def has_permission_to_view_admins_data(self, obj):
        return self.is_authenticated and self.is_admin and obj == self

    def has_permission_to_edit_admins_data(self, obj):
        return self.has_admin_permission(obj)

    def has_permission_to_delete_admins_data(self, obj):
        return self.has_admin_permission(obj)

    def has_permission_to_update_admins_data(self, obj):
        return self.has_admin_permission(obj)

    def has_permission_to_view_group_data(self, obj):
        return self.is_authenticated and obj in self.groups.all()

    def has_permission_to_edit_group_data(self, obj):
        return self.has_permission_to_view_group_data(obj)

    def has_permission_to_delete_group_data(self, obj):
        return self.has_permission_to_view_group_data(obj)

    def has_permission_to_update_group_data(self, obj):
        return self.has_permission_to_view_group_data(obj)
