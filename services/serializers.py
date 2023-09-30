from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email',
                  'password', 'country', 'phone_number', 'profile_image', 'created_at', 'updated_at']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_image = validated_data.pop('profile_image', None)
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            country=validated_data.get('country', ''),
            phone_number=validated_data.get('phone_number', ''),
        )

        if profile_image:
            user.profile_image = profile_image

        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_country(self, value):
        return value.capitalize()


class CartItemSerializer(serializers.Serializer):
    item_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


# {
#     "username" : "temp",
#     "email" : "temp@gmail.com",
#     "first_name" : "first",
#     "last_name" : "temp",
#     "password" : "aryan1234",
#     "country" : "USA",
#     "phone_number" : "8957760502"
# }

# {
#     "email": "temp@gmail.com",
#     "password": "aryan1234"
# }
