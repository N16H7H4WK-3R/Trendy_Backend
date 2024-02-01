from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import (
    AuthUserRegistrationView,
    AuthUserLoginView,
    UserListView,
    AuthAdminRegistrationView,
)

urlpatterns = [
    path("token/obtain/", jwt_views.TokenObtainPairView.as_view(), name="token_create"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", AuthUserRegistrationView.as_view(), name="register"),
    path("register/admin/", AuthAdminRegistrationView.as_view(), name="register_admin"),
    path("login/", AuthUserLoginView.as_view(), name="login"),
    path("users/", UserListView.as_view(), name="users"),
]
