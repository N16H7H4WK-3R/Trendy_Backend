from django.contrib import admin
from .models import CustomUser, CartItem, FavoriteItem, OrderItem, Product


class CartItemAdmin(admin.TabularInline):
    model = CartItem
    extra = 0


class FavoriteItemAdmin(admin.TabularInline):
    model = FavoriteItem
    extra = 0

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    extra = 0

# Custom admin class for CustomUser
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "is_superuser", "email", "first_name", "last_name")
    inlines = [CartItemAdmin, FavoriteItemAdmin, OrderItemAdmin]


# Custom admin class for Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ("productTitle", "id", "productPrice")


# Registere models
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Product, ProductAdmin)
