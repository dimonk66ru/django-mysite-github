from django.urls import path
from django.contrib.auth.views import LoginView
from .views import (
    get_cookie_view,
    set_cookie_view,
    set_session_view,
    get_session_view,
    MyLoginView,
    MyLogoutView,
    AboutMeView,
    RegisterView,
    FooBarView,
    ProfileUpdateView,
    ProfilesListView,
    ProfileView,
    HelloView
)

app_name = "myauth"

urlpatterns = [
    # path("login/", LoginView.as_view(
    #     redirect_authenticated_user=True,
    # ), name="login"),
    path("login/", MyLoginView.as_view(), name="login"),
    path("hello/", HelloView.as_view(), name="hello"),
    path("logout/", MyLogoutView.as_view(), name="logout"),
    path("cookie/get/", get_cookie_view, name="cookie-get"),
    path("cookie/set/", set_cookie_view, name="cookie-set"),
    path("session/get/", get_session_view, name="session-get"),
    path("session/set/", set_session_view, name="session-set"),
    path("about-me/", AboutMeView.as_view(), name="about-me"),
    path("register/", RegisterView.as_view(), name="register"),
    path("about-me/update/<int:pk>", ProfileUpdateView.as_view(), name="profile-update"),
    path("foo-bar/", FooBarView.as_view(), name="foo-bar"),
    path("profiles/", ProfilesListView.as_view(), name="profiles-list"),
    path("profiles/<int:pk>/", ProfileView.as_view(), name="profile-details"),
]
