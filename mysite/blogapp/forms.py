from django import forms
from .models import Article
from django.forms import ModelForm


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = "title", "content", "pub_date", "author", "category", "tags",
