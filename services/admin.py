from django.contrib import admin
from .models import (
    CustomUser,
    CartItem,
    FavoriteItem,
    Product,
    Order,
    OrderItem,
)


class CartItemAdmin(admin.TabularInline):
    model = CartItem
    extra = 0


class FavoriteItemAdmin(admin.TabularInline):
    model = FavoriteItem
    extra = 0


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    extra = 0




class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "order_date",
        "payment_status",
        "order_status",
        "delivery_status",
    )
    inlines = [OrderItemAdmin]


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "is_superuser", "email", "first_name", "last_name")
    inlines = [CartItemAdmin, FavoriteItemAdmin]


class ProductAdmin(admin.ModelAdmin):
    list_display = ("productTitle", "id", "productPrice")


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
