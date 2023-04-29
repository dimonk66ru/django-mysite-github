from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MyauthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myauth'
    verbose_name = _('authentication')
