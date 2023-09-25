from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model, authenticate
from django.db import IntegrityError
from .serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer

User = get_user_model()


@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.create_user(**serializer.validated_data)
            except IntegrityError:
                return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, username=email, password=password)
        if user:
            # Generate and return an authentication token here
            # You can use Django Rest Framework's TokenAuthentication for this
            return Response({'token': 'YOUR_AUTH_TOKEN'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_profile(request):
    if request.method == 'PUT':
        serializer = UserUpdateSerializer(
            request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Profile updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from rest_framework import generics, permissions, status
# from rest_framework.response import Response
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
# from .models import Customers
# from .serializers import CustomersSerializer
# from django.contrib.auth.hashers import make_password


# class SignUpView(generics.CreateAPIView):
#     queryset = Customers.objects.all()
#     serializer_class = CustomersSerializer
#     permission_classes = [permissions.AllowAny]

#     def perform_create(self, serializer):
#         # Ensure the provided password is hashed
#         serializer.validated_data['password'] = make_password(
#             serializer.validated_data['password'])
#         serializer.save()


# class LoginView(ObtainAuthToken):
#     pass


# class EditProfileView(generics.RetrieveUpdateAPIView):
#     queryset = Customers.objects.all()
#     serializer_class = CustomersSerializer
#     permission_classes = [permissions.IsAuthenticated]
