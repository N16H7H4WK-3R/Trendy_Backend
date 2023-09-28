from django.urls import path
from .views import register_user, user_login, user_logout, edit_profile, fetch_user_data

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('user/', fetch_user_data, name='user_data'),
    
]
