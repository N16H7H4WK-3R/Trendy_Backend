from django.urls import path
from .views import register_user, user_login, user_logout, edit_profile, fetch_user_data, fetch_productData, fetch_productDetailData, add_to_cart

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('user/', fetch_user_data, name='user_data'),
    path('data/', fetch_productData, name='product_data'),
    path('detail/<str:product_id>/', fetch_productDetailData, name='product_detail_data'),
    path('cart/', add_to_cart, name='cart'),
]
