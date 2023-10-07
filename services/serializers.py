from rest_framework import serializers
from .models import CustomUser, CartItem, FavoriteItem, Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "country",
            "phone_number",
            "profile_image",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        profile_image = validated_data.pop("profile_image", None)
        user = CustomUser(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            country=validated_data.get("country", ""),
            phone_number=validated_data.get("phone_number", ""),
        )

        if profile_image:
            user.profile_image = profile_image

        user.set_password(validated_data["password"])
        user.save()
        return user

    def validate_country(self, value):
        return value.capitalize()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "productPrice",
            "category",
            "productTitle",
            "productDescription",
            "imageUrl",
            "imageUrl1",
            "imageUrl2",
            "imageUrl3",
        ]

    def create(self, validated_data):
        return Product.objects.create(**validated_data)


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "productPrice",
            "category",
            "productTitle",
            "productDescription",
            "imageUrl",
            "imageUrl1",
            "imageUrl2",
            "imageUrl3",
        ]


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer()

    class Meta:
        model = CartItem
        fields = ["id", "user", "product", "quantity", "added_at"]

    def create(self, validated_data):
        return CartItem.objects.create(**validated_data)


class FavoriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = ["product_id", "product", "added_at"]
