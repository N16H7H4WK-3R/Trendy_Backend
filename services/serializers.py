from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'role')


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'role')


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'role')


# from rest_framework import serializers
# from .models import Customers


# class CustomersSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)  # Add this line

#     class Meta:
#         model = Customers
#         fields = ('id', 'username', 'email', 'password',
#                   'first_name', 'last_name', 'bio')
