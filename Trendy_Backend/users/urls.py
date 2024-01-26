from django.urls import path
from .views import (
    register_user_view,
    login_user_view,
    fetch_user_details_view,
)

urlpatterns = [
    path("register/", register_user_view, name="register"),
    path("login/", login_user_view, name="login"),
    path("user/details/", fetch_user_details_view, name="fetch-user-details"),
]
