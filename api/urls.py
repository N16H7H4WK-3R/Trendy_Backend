from django.urls import path
from home.views import user_registration, user_login, edit_profile

urlpatterns = [
    path('signup/', user_registration, name='signup'),
    path('login/', user_login, name='login'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]
