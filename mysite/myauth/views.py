from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import reverse, get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView
from django.views import View
from random import random
from .models import Profile
import logging


logger = logging.getLogger(__name__)


class HelloView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("<h1>Hello world</h1>")


class MyLoginView(LoginView):
    template_name = "myauth/login.html"
    redirect_authenticated_user = True

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            logger.info(f'авторизовался пользователь: {user_name}')
        return super().post(self, request, *args, **kwargs)


class AboutMeView(TemplateView):
    template_name = "myauth/about-me.html"


class ProfilesListView(ListView):
    template_name = "myauth/profiles-list.html"
    model = Profile
    context_object_name = "profiles"


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "myauth/register.html"
    success_url = reverse_lazy("myauth:about-me")

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)
        return response


class ProfileUpdateView(UserPassesTestMixin, UpdateView):
    def test_func(self):
        if self.request.user.is_staff:
            return True
        profile_obj = get_object_or_404(Profile, pk=self.kwargs.get('pk'))
        if profile_obj.pk == self.request.user.profile.pk:
            return True

    model = Profile
    fields = "bio", "avatar"
    template_name = "myauth/profile_update_form.html"
    success_url = reverse_lazy("myauth:about-me")


class ProfileView(DetailView):
    template_name = "myauth/profile-details.html"
    model = Profile
    context_object_name = "profile"


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("myauth:login")


@user_passes_test(lambda u: u.is_superuser)
def set_cookie_view(request: HttpRequest) -> HttpResponse:
    response = HttpResponse("Cookie set")
    response.set_cookie("fizz", "buzz", max_age=3600)
    return response


@cache_page(60 * 2)
def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get("fizz", "default value")
    return HttpResponse(f"Cookie value: {value!r} + {random()}")


@permission_required("myauth.view_profile", raise_exception=True)
def set_session_view(request: HttpRequest) -> HttpResponse:
    request.session["foobar"] = "spameggs"
    return HttpResponse("Session set!")


@login_required
def get_session_view(request: HttpRequest) -> HttpResponse:
    value = request.session.get("foobar", "default")
    return HttpResponse(f"Session value: {value!r}")


class FooBarView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        return JsonResponse({"foo": "bar", "spam": "eggs"})
