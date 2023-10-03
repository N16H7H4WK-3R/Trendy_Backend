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
    product_id = models.IntegerField()
    product_price = models.IntegerField(default=0)
    product_image_url = models.CharField(max_length=500, default='')
    quantity = models.PositiveIntegerField()
    added_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Cart item for {self.user}: Item ID {self.product_id}, Quantity {self.quantity}'

    @classmethod
    def add_to_cart(cls, user, product_id, quantity, product_price, product_image_url):
        cart_item, created = cls.objects.get_or_create(
            user=user,
            product_id=product_id,
            defaults={
                'quantity': quantity,
                'product_price': product_price,
                'product_image_url': product_image_url,
            }
        )

        # If the item already exists, update the quantity
        if not created:
            cart_item.quantity += quantity
            cart_item.save()