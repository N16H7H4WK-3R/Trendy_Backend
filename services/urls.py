from django.urls import path
from . import views

app_name = "services"

urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("delete-profile/", views.delete_profile, name="delete_profile"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("user/", views.fetch_user_data, name="user_data"),
    path("add-product/", views.add_product, name="add_product"),
    path("data/", views.fetch_productData, name="product_data"),
    path("detail/<str:id>/", views.fetch_productDetailData, name="product_detail_data"),
    path("cart/", views.add_to_cart, name="cart"),
    path("cart-data/", views.fetch_user_cart_data, name="user_cart_data"),
    path("cart-delete/", views.remove_from_cart, name="remove_from_cart"),
    path(
        "cart-update/",
        views.update_cart_item_quantity,
        name="update_cart_item_quantity",
    ),
]
