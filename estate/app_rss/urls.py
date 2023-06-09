from django.urls import path
from app_rss.feeds import LatestNewsFeed

app_name = "app_rss"

urlpatterns = [
    path('latest/feed/', LatestNewsFeed(), name='rss'),
]
