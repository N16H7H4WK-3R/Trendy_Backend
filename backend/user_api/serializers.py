from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


# CUSTOMER REGISTRATION SERIALIZER
class CustomerRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "mobile_number", "email", "password")

    def create(self, validated_data):
        auth_user = User.objects.create_customer(**validated_data)
        return auth_user


# ADMIN REGISTRATION SERIALIZER
class AdminRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "mobile_number",
            "email",
            "password",
            "role",
        )

    def create(self, validated_data):
        auth_user = User.objects.create_superuser(**validated_data)
        return auth_user


# ADMIN REGISTRATION SERIALIZER
class SellerRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "mobile_number",
            "email",
            "password",
            "role",
        )

    def create(self, validated_data):
        auth_user = User.objects.create_seller(**validated_data)
        return auth_user


# USER LOGIN SERIALIZER
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        email = data["email"]
        password = data["password"]
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            update_last_login(None, user)

            validation = {
                "access": access_token,
                "refresh": refresh_token,
                "email": user.email,
                "role": user.role,
            }

            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")


# USER LIST SERIALIZER ( FOR ADMIN ONLY )
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "role",
            "email",
            "first_name",
            "last_name",
            "mobile_number",
            "date_joined",
        )
