from django.contrib import admin
from .models import CustomUser, CartItem, FavoriteItem, Product


class CartItemAdmin(admin.TabularInline):
    model = CartItem
    extra = 0


class FavoriteItemAdmin(admin.TabularInline):
    model = FavoriteItem
    extra = 0


# Custom admin class for CustomUser
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("is_superuser", "username", "email", "first_name", "last_name")
    inlines = [CartItemAdmin, FavoriteItemAdmin]


# Custom admin class for Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "productTitle", "productPrice")


# Registere models
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Product, ProductAdmin)
