from django.shortcuts import render
from django.views.generic import ListView
from .models import Article


class ArticleListView(ListView):
    template_name = "blogapp/articles_list.html"
    # model = Article
    queryset = (
        Article.objects
        .select_related("author")
        .prefetch_related("tags")
        .prefetch_related("category")
        .defer("content", "author__bio")
    )

