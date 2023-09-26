from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            country=validated_data.get('country', ''),
            phone_number=validated_data.get('phone_number', ''),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_country(self, value):
        return value.capitalize()


# {
#     "username" : "temp",
#     "email" : "temp@gmail.com",
#     "first_name" : "first",
#     "last_name" : "temp",
#     "password" : "aryan1234"
# }

# {
#     "email": "temp@gmail.com",
#     "password": "aryan1234"
# }





# @api_view(['POST'])
# def user_login(request):
#     if request.method == 'POST':
#         username = request.data.get('username')
#         password = request.data.get('password')
