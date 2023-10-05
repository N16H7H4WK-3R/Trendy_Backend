from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50, default="INDIA")
    phone_number = models.CharField(max_length=18, default="", null=False, blank=False)
    profile_image = models.ImageField(
        upload_to="profile_images/", null=True, blank=True
    )
    created_at = models.DateTimeField(
        default=timezone.localtime, editable=False, blank=True
    )
    updated_at = models.DateTimeField(auto_now=True)
    cart_items = models.ManyToManyField(
        "Product", through="CartItem", related_name="users_cart", blank=True
    )
    favorite_items = models.ManyToManyField(
        "Product", through="FavoriteItem", related_name="users_favorite", blank=True
    )

    def __str__(self):
        return self.username


class Product(models.Model):
    title = models.CharField(max_length=500, default="")
    price = models.IntegerField(default=0)
    image_url = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.title


class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Cart item for {self.user} || Product: {self.product} || Quantity: {self.quantity}"


class FavoriteItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    added_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Favorite item for {self.user} || Product: {self.product}"


# {
#     "username" : "temp",
#     "email" : "temp@gmail.com",
#     "first_name" : "first",
#     "last_name" : "temp",
#     "password" : "aryan1234",
#     "country" : "USA",
#     "phone_number" : "8957760502"
# }

# {
#     "email": "temp@gmail.com",
#     "password": "aryan1234"
# }
