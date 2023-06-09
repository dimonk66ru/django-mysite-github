from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import reverse, get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView
from django.views import View
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.models import User


class MyLoginView(LoginView):
    template_name = "myauth/login.html"
    redirect_authenticated_user = True


class ProfilesListView(ListView):
    template_name = "myauth/profiles-list.html"
    model = Profile
    context_object_name = "profiles"


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "myauth/register.html"
    success_url = reverse_lazy("myauth:profile-details")

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

    def get_success_url(self):
        return reverse(
            "myauth:profile-details",
            kwargs={"pk": self.object.pk}
        )


class ProfileUpdateView(UserPassesTestMixin, UpdateView):
    def test_func(self):
        if self.request.user.is_staff:
            return True
        profile_obj = get_object_or_404(Profile, pk=self.kwargs.get('pk'))
        if profile_obj.pk == self.request.user.profile.pk:
            return True

    model = Profile
    fields = "bio", "avatar", "phone"
    template_name = "myauth/profile_update_form.html"

    def get_success_url(self):
        return reverse(
            "myauth:profile-details",
            kwargs={"pk": self.object.pk}
        )


class ProfileView(DetailView):
    template_name = "myauth/profile-details.html"
    model = Profile
    context_object_name = "profile"

    def get_success_url(self):
        return reverse(
            "myauth:profile-details",
            kwargs={"pk": self.object.pk}
        )


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("myauth:login")
