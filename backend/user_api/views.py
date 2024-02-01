from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import (
    CustomerRegistrationSerializer,
    UserLoginSerializer,
    UserListSerializer,
    AdminRegistrationSerializer,
    SellerRegistrationSerializer,
)
from .models import User


class RegistrationBaseView(APIView):
    serializer_class = None
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                "success": True,
                "statusCode": status_code,
                "message": f"{self.role} successfully registered!",
            }

            return Response(response, status=status_code)
        else:
            status_code = status.HTTP_400_BAD_REQUEST

            response = {
                "success": False,
                "statusCode": status_code,
                "message": f"{self.role} registration failed!",
                "user": serializer.errors,
            }

            return Response(response, status=status_code)


class CustomerRegistrationView(RegistrationBaseView):
    serializer_class = CustomerRegistrationSerializer
    role = "Customer"


class AdminRegistrationView(RegistrationBaseView):
    serializer_class = AdminRegistrationSerializer
    role = "Admin"


class SellerRegistrationView(RegistrationBaseView):
    serializer_class = SellerRegistrationSerializer
    role = "Seller"


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK
            email = serializer.data["email"]

            response = {
                "success": True,
                "statusCode": status_code,
                "message": f" logged in successfully as {email} ",
                "access": serializer.data["access"],
                "refresh": serializer.data["refresh"],
            }

            return Response(response, status=status_code)


class UserListView(APIView):
    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        if user.role != 1:
            response = {
                "success": False,
                "status_code": status.HTTP_403_FORBIDDEN,
                "message": "You are not authorized to perform this action",
            }
            return Response(response, status.HTTP_403_FORBIDDEN)
        else:
            users = User.objects.all()
            serializer = self.serializer_class(users, many=True)
            response = {
                "success": True,
                "status_code": status.HTTP_200_OK,
                "message": "Successfully fetched users",
                "users": serializer.data,
            }
            return Response(response, status=status.HTTP_200_OK)
