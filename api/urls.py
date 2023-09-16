from django.urls import path
from home.views import user_registration, user_login

urlpatterns = [
    path('signup/', user_registration, name='signup'),
    path('login/', user_login, name='login'),
]
