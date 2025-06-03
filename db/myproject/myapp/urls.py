from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    home_view,
    signup,
    login,
    logout,
)

urlpatterns = [
    path("", home_view),
    path("signup/", signup, name="signup"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
]