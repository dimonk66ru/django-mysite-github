from django.urls import path
from .views import (
    MyLoginView,
    MyLogoutView,
    RegisterView,
    ProfileUpdateView,
    ProfilesListView,
    ProfileView,
)

app_name = "myauth"

urlpatterns = [
    path("login/", MyLoginView.as_view(), name="login"),
    path("logout/", MyLogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profiles/", ProfilesListView.as_view(), name="profiles"),
    path("profiles/<int:pk>/", ProfileView.as_view(), name="profile-details"),
    path("profiles/update/<int:pk>", ProfileUpdateView.as_view(), name="profile-update"),
]
