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
    productPrice = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    category = models.CharField(max_length=255, default="")
    productTitle = models.CharField(max_length=255, default="")
    productDescription = models.TextField(default="")
    imageUrl = models.URLField(max_length=2000, default="")
    imageUrl1 = models.URLField(max_length=2000, default="")
    imageUrl2 = models.URLField(max_length=2000, default="")
    imageUrl3 = models.URLField(max_length=2000, default="")

    def __str__(self):
        return self.productTitle


class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="cart_items"
    )
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


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now)
    payment_status = models.CharField(max_length=50, default="PENDING")
    order_status = models.CharField(max_length=50, default="PENDING")
    delivery_status = models.CharField(max_length=50, default="PENDING")

    def __str__(self):
        return f"Order for {self.user} || Order Date: {self.order_date}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    shipping_address = models.CharField(max_length=255, default="")
    payment_details = models.CharField(max_length=255, default="")

    def __str__(self):
        return f"Order item for {self.order.user} || Product: {self.product}"


class PaymentDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=255, default="")
    transaction_id = models.CharField(max_length=255, default="", unique=True)
    payment_status = models.CharField(max_length=50, default="PENDING")
    payment_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Payment details for {self.order.user} || Payment Method: {self.payment_method}"


class ShippingAddress(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, default="")
    city = models.CharField(max_length=255, default="")
    state = models.CharField(max_length=255, default="")
    zipcode = models.CharField(max_length=255, default="")
    country = models.CharField(max_length=255, default="")

    def __str__(self):
        return f"Shipping address for {self.order.user} || Address: {self.address}"
