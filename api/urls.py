from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import home

urlpatterns = [
    path('', home),
    path('category/', include('api.category.urls')),
    path('user/', include('api.user.urls')),
]
