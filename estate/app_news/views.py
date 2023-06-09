from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import NewsItem


def get_news_in_custom_format(reqeust):
    format = reqeust.GET['format']
    if format not in ['xml', 'json', 'yaml']:
        return HttpResponseBadRequest()
    data = serializers.serialize(format, NewsItem.objects.all())
    return HttpResponse(data)


class NewsItemDetailView(DetailView):
    model = NewsItem
    template_name = "app_news/newsitem_detail.html"


class NewsListView(ListView):
    model = NewsItem
    template_name = "app_news/news.html"