from django.urls import path
from .views import SignUpView, LoginView, EditProfileView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('edit-profile/', EditProfileView.as_view(), name='edit-profile'),
]
