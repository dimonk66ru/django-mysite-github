from django.contrib.sitemaps import Sitemap
from app_news.models import NewsItem


class NewsSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return NewsItem.objects.filter(is_published=True).all()

    def lastmod(self, obj: NewsItem):
        return obj.published_at
