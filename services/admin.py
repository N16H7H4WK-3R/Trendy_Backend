from django.contrib import admin
from .models import CustomUser, CartItem

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(CartItem)