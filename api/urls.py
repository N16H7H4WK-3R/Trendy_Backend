from django.urls import path
from home.views import index , login

urlpatterns = [
    path('index/', index),
    path('login/', login),
]