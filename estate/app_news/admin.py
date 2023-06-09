from django.contrib import admin
from .models import NewsItem


@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = "id", "title", "text", "is_published", "created_at"
