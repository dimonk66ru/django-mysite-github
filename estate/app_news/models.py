from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class NewsItem(models.Model):
    class Meta:
        verbose_name = _("news")

    def __str__(self):
        return self.title

    title = models.CharField(max_length=128, verbose_name=_("title"))
    text = models.TextField(blank=True, verbose_name=_("text news"))
    is_published = models.BooleanField(default=False, verbose_name=_("is published"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))
    description = models.TextField(blank=True, verbose_name=_("description"))
    published_at = models.DateTimeField(null=True, verbose_name=_("published at"))

    def get_absolute_url(self):
        return reverse('detail_news', args=[str(self.id)])
