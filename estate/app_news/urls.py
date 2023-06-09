from django.urls import path
from .views import get_news_in_custom_format, NewsItemDetailView, NewsListView


app_name = "app_news"

urlpatterns = [
    path("", get_news_in_custom_format, name="news_list"),
    path("news/", NewsListView.as_view(), name="news"),
    path("<int:pk>", NewsItemDetailView.as_view(), name="detail_news")
]
