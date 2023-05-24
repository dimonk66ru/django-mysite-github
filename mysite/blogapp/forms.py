from django import forms
from .models import Article
from django.contrib.auth.models import Group
from django.forms import ModelForm


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        # fields = "name", "price", "description", "discount", "preview"
