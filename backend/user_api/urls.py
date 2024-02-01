from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import (
    CustomerRegistrationView,
    UserLoginView,
    UserListView,
    AdminRegistrationView,
    SellerRegistrationView,
)

urlpatterns = [
    path("token/obtain/", jwt_views.TokenObtainPairView.as_view(), name="token_create"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", CustomerRegistrationView.as_view(), name="register"),
    path("register/admin/", AdminRegistrationView.as_view(), name="register_admin"),
    path("register/seller/", SellerRegistrationView.as_view(), name="register_seller"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("users/", UserListView.as_view(), name="users"),
]
