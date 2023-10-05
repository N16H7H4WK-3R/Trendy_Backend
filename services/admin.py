from django.contrib import admin
from .models import CustomUser, CartItem, FavoriteItem, Product

# Custom admin classes for CartItem and FavoriteItem
class CartItemAdmin(admin.TabularInline):
    model = CartItem
    extra = 0

class FavoriteItemAdmin(admin.TabularInline):
    model = FavoriteItem
    extra = 0

# Custom admin class for CustomUser
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    inlines = [CartItemAdmin, FavoriteItemAdmin]

# Register your models with the custom admin classes
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Product)  # Register the Product model separately
