from django import forms
from .models import Profile
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "bio", "phone", "avatar"

