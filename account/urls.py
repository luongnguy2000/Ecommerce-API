from rest_framework import routers
from django.urls import path, include
from .views import *

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("updateuser/", UpdateUser.as_view(), name="updateUser"),
    path("updateprofile/", UpdateProfile.as_view(), name="updateProfile")
]

