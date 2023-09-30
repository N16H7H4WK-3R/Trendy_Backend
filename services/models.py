from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50, default='INDIA')
    phone_number = models.CharField(
        max_length=18, default='', null=False, blank=False)
    profile_image = models.ImageField(
        upload_to='profile_images/', null=True, blank=True)
    created_at = models.DateTimeField(
        default=timezone.localtime, editable=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.username}'


class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item_id = models.IntegerField()
    quantity = models.PositiveIntegerField()
    added_at = models.DateTimeField(default=timezone.localtime)

    def __str__(self):
        return f'Cart item for {self.user} : Item ID {self.item_id}, Quantity {self.quantity}'

    @classmethod
    def add_to_cart(cls, user, item_id, quantity):
        existing_item = cls.objects.filter(user=user, item_id=item_id).first()

        if existing_item:
            existing_item.quantity += quantity
            existing_item.save()
        else:
            cls.objects.create(user=user, item_id=item_id, quantity=quantity)
