"""estate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from app_news.sitemap import NewsSitemap

sitemaps = {
    'news': NewsSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('myauth.urls')),
    path('market/', include('market.urls')),
    path('news/', include('app_news.urls')),
    path('rss/', include('app_rss.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('i18n', include('django.conf.urls.i18n')),
]
