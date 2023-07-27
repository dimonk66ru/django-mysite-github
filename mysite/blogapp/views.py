import os.path
from django.contrib.syndication.views import Feed
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from .forms import ArticleForm
from .models import Article
import logging


logger = logging.getLogger(__name__)


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

    def dispatch(self, request, *args, **kwargs):
        logger.info('Вызывается Список статей')
        return super().dispatch(request, *args, **kwargs)


class ArticleDetailView(DetailView):
    template_name = "blogapp/article_detail.html"
    queryset = (
        Article.objects
        .select_related("author")
        .prefetch_related("tags")
        .prefetch_related("category")
    )

    def dispatch(self, request, *args, **kwargs):
        u = self.request.user
        i = os.path.split(self.request.path)
        i_1 = os.path.split(i[0])
        i = i_1[1]
        logger.info(f'{u} вызывает статью с ID# {i}')
        return super().dispatch(request, *args, **kwargs)


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy("blogapp:articles")

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        u = self.request.user
        if form.is_valid():
            logger.info(f'{u} создал новую статью')
        return super().post(request, *args, **kwargs)


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse(
            "blogapp:article_detail",
            kwargs={"pk": self.object.pk}
        )


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("blogapp:articles")


class LatestArticleFeed(Feed):
    title = "Blog articles (latest)"
    description = "Updates on changes and addition blog articles"
    link = reverse_lazy("blogapp:articles")

    def items(self):
        return (
            Article.objects
            .filter(pub_date__isnull=False)
            .order_by("-pub_date")[:5]
        )

    def item_title(self, item: Article):
        return item.title

    def item_description(self, item: Article):
        return item.content[:200]

    def item_link(self, item: Article):
        return reverse("blogapp:article_detail", kwargs={"pk": item.pk})