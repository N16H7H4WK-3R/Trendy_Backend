from rest_framework import generics, permissions
from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.contrib.auth.hashers import make_password


class SignUpView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        # Ensure the provided password is hashed
        serializer.validated_data['password'] = make_password(
            serializer.validated_data['password'])
        serializer.save()


class LoginView(ObtainAuthToken):
    pass


class EditProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
