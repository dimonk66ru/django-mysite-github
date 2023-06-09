from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


def avatar_directory_path(instance: "Profile", filename: str) -> str:
    return "profiles/profile_{pk}/avatar/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


class Profile(models.Model):
    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self):
        return self.user.username

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("user"))
    bio = models.TextField(max_length=500, blank=True, verbose_name=_("bio"))
    phone = models.CharField(max_length=12, blank=True, verbose_name=_("phone"))
    avatar = models.ImageField(null=True, blank=True, upload_to=avatar_directory_path, verbose_name=_("avatar"))
