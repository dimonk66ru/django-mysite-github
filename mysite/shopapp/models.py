from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


def product_preview_directory_path(instance: "Product", filename: str) -> str:
    return "products/product_{pk}/preview/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


class Product(models.Model):
    class Meta:
        ordering = ["name", "price"]
        verbose_name = _("product")
        verbose_name_plural = _("products")

    name = models.CharField(max_length=100, verbose_name=_("name"), db_index=True)
    description = models.TextField(null=False, blank=True, verbose_name=_("description"), db_index=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name=_("price"))
    discount = models.PositiveSmallIntegerField(default=0, verbose_name=_("discount"))
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_("created by"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))
    archived = models.BooleanField(default=False, verbose_name=_("archived"))
    preview = models.ImageField(null=True, blank=True, upload_to=product_preview_directory_path, verbose_name=_("preview"))

    def __str__(self) -> str:
        p = _("Product")
        return f"{p}(id={self.id} {self.name!r})"


def product_images_directory_path(instance: "ProductImage", filename: str) -> str:
    return "products/product_{pk}/images/{filename}".format(
        pk=instance.product.pk,
        filename=filename,
    )


class ProductImage(models.Model):
    class Meta:
        verbose_name = _("product image")
        verbose_name_plural = _("product images")

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to=product_images_directory_path)
    description = models.CharField(max_length=200, null=False, blank=True)


class Order(models.Model):
    class Meta:
        verbose_name = _("order")
        verbose_name_plural = _("orders")

    def __str__(self):
        o = _("order")
        return f'{o}: {self.pk}'

    delivery_address = models.TextField(null=False, blank=True, verbose_name=_("delivery address"))
    promocode = models.CharField(max_length=20, null=False, blank=True, verbose_name=_("promocode"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_("user"))
    products = models.ManyToManyField(Product, related_name="orders", verbose_name=_("products"))
    receipt = models.FileField(null=True, upload_to="orders/receipts/", verbose_name=_("receipt"))
