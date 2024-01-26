from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import UserSerializer


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def register_user_view(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user_type = request.data.get("user_type", "").lower()
            if user_type not in dict(CustomUser.USER_TYPE_CHOICES).keys():
                return Response(
                    {"detail": "Invalid user_type."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if CustomUser.objects.filter(email=request.data["email"]).exists():
                return Response(
                    {"detail": "Email is already in use."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if CustomUser.objects.filter(username=request.data["username"]).exists():
                return Response(
                    {"detail": "Username is already in use."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Save the user
            serializer.save()

            # Generate JWT token and include it in the response
            user = CustomUser.objects.get(username=request.data["username"])
            refresh = RefreshToken.for_user(user)
            token = str(refresh.access_token)

            return Response(
                {
                    "user": serializer.data,
                    "token": token,
                    "detail": "Account created successfully.",
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def login_user_view(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Generate JWT token and include it in the response
            user = CustomUser.objects.get(username=request.data["username"])
            refresh = RefreshToken.for_user(user)
            token = str(refresh.access_token)

            return Response(
                {
                    "token": token,
                    "detail": "Login successful.",
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def fetch_user_details_view(request):
    try:
        print(request.auth)  # This will print the token information
        user = request.user
        print(user)  # This will print the user information
        serializer = UserSerializer(user)
        return Response({"user": serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
