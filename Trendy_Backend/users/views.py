from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import UserSerializer, AdminUserSerializer
from django.contrib.auth.decorators import user_passes_test


#####################################
####### ____NORMAL USER____#########
#####################################


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def register_user_view(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user_type = request.data.get("user_type", "").lower()
            if user_type != "user":
                return Response(
                    {"detail": "Invalid user_type for user registration."},
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


#####################################
######### ___ADMIN USER____##########
#####################################


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def register_admin_user_view(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user_type = request.data.get("user_type", "").lower()
            if user_type != "admin":
                return Response(
                    {"detail": "Invalid user_type for admin registration."},
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

            # Save the user as an admin
            serializer.save(is_staff=True, is_superuser=True)

            # Generate JWT token and include it in the response
            user = CustomUser.objects.get(username=request.data["username"])
            refresh = RefreshToken.for_user(user)
            token = str(refresh.access_token)

            return Response(
                {
                    "user": serializer.data,
                    "token": token,
                    "detail": "Admin account created successfully.",
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def fetch_admin_user_details_view(request):
    try:
        if not request.user.is_admin:
            return Response(
                {"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN
            )

        users = CustomUser.objects.all()
        serializer = AdminUserSerializer(users, many=True)
        return Response({"users": serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def login_admin_user_view(request):
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
                    "detail": "Login successful. Welcome Admin",
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


#####################################
###### ___SELLERS / VENDER____#######
#####################################


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def register_seller_user_view(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user_type = request.data.get("user_type", "").lower()
            if user_type != "seller":
                return Response(
                    {"detail": "Invalid user_type for seller registration."},
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

            # Save the user as a seller
            serializer.save()

            # Assign seller privileges
            user = CustomUser.objects.get(username=request.data["username"])
            user.is_staff = True
            user.save()

            # Generate JWT token and include it in the response
            refresh = RefreshToken.for_user(user)
            token = str(refresh.access_token)

            return Response(
                {
                    "user": serializer.data,
                    "token": token,
                    "detail": "Seller account created successfully.",
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def fetch_seller_user_details_view(request):
    try:
        if not request.user.is_seller:
            return Response(
                {"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN
            )

        users = CustomUser.objects.all()
        serializer = AdminUserSerializer(users, many=True)
        return Response({"users": serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def login_seller_user_view(request):
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
                    "detail": "Login successful. Welcome Seller",
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
