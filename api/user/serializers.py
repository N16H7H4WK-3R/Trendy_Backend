from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Add this line

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password',
                  'first_name', 'last_name', 'bio')
