from django.urls import path
from .views import (
    register_user,
    user_login,
    user_logout,
    edit_profile,
    fetch_user_data,
    add_product,
    fetch_productData,
    fetch_productDetailData,
    add_to_cart,
    fetch_user_cart_data,
    remove_from_cart,
    update_cart_item_quantity,
)


urlpatterns = [
    path("register/", register_user, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("edit-profile/", edit_profile, name="edit_profile"),
    path("user/", fetch_user_data, name="user_data"),
    path("add-product/", add_product, name="add_product"),
    path("data/", fetch_productData, name="product_data"),
    path(
        "detail/<str:productNumber>/", fetch_productDetailData, name="product_detail_data"
    ),
    path("cart/", add_to_cart, name="cart"),
    path("cart-data/", fetch_user_cart_data, name="user_cart_data"),
    path("cart-delete/", remove_from_cart, name="remove_from_cart"),
    path("cart-update/", update_cart_item_quantity, name="update_cart_item_quantity"),
]
