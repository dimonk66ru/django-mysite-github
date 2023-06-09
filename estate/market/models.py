from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class RoomCount(models.Model):
    class Meta:
        verbose_name = _("room count")

    def __str__(self):
        return str(self.room_count)

    room_count = models.PositiveIntegerField(default=0, verbose_name=_("room count"))


class EstateType(models.Model):
    class Meta:
        verbose_name = _("estate type")

    def __str__(self):
        return self.estate_type

    estate_type = models.CharField(max_length=20, verbose_name=_("estate type"))


class Estate(models.Model):
    class Meta:
        verbose_name = _("estate")

    address = models.TextField(null=False, blank=True, verbose_name=_("address"))
    price = models.DecimalField(default=0, max_digits=20, decimal_places=0, verbose_name=_("price"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))
    seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("seller"))
    estate_type = models.ForeignKey(EstateType, on_delete=models.CASCADE, verbose_name=_("estate type"))
    room_count = models.ForeignKey(RoomCount, on_delete=models.CASCADE, verbose_name=_("room count"))
