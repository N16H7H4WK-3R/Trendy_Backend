from django.urls import path
from .views import (
    RegisterUserView,
    UserDetailsView,
    UserProfileUpdateView,
    ChangePasswordView,
)

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path("user/", UserDetailsView.as_view(), name="user-details"),
    path("user/update/", UserProfileUpdateView.as_view(), name="user-update"),
    path("user/change-password/", ChangePasswordView.as_view(), name="change-password"),
]
