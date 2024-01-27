# user app/urls.py
from django.urls import path
from .views import (
    register_user_view,
    login_user_view,
    fetch_user_details_view,
    fetch_admin_user_details_view,
    fetch_seller_user_details_view,
    register_admin_user_view,
    register_seller_user_view,
    login_admin_user_view,
    login_seller_user_view,
)

urlpatterns = [
    # REGISTERATION URLS
    path("register/", register_user_view, name="register"),
    path("register/admin/", register_admin_user_view, name="register-admin"),
    path("register/seller/", register_seller_user_view, name="register-seller"),
    # LOGIN URLS
    path("login/", login_user_view, name="login"),
    path("login/admin/", login_admin_user_view, name="login-admin"),
    path("login/seller/", login_seller_user_view, name="login-seller"),
    # FETCH USER DETAILS URLS
    path("user/details/", fetch_user_details_view, name="fetch-user-details"),
    path(
        "admin/details/",
        fetch_admin_user_details_view,
        name="fetch-admin-user-details",
    ),
    path(
        "seller/details/",
        fetch_seller_user_details_view,
        name="fetch-seller-user-details",
    ),
]
