from django.contrib import admin
from .models import Article, Tag, Category, Author
from django.utils.translation import gettext_lazy as _


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "bio",


admin.site.register(Category)
admin.site.register(Tag)


class TagsInline(admin.TabularInline):
    model = Article.tags.through


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        TagsInline,
    ]
    list_display = "pk", "title", "content", "pub_date", "author", "category"
