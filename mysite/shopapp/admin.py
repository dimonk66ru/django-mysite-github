from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from .models import Product, Order, ProductImage
from .admin_mixins import ExportAsCSVMixin
from django.utils.translation import gettext, gettext_lazy as _


class OrderInline(admin.StackedInline):
    model = Product.orders.through


class ProductInLine(admin.TabularInline):
    model = ProductImage


@admin.action(description=_("Archive products"))
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)


@admin.action(description=_("Unarchive products"))
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [
        mark_archived,
        mark_unarchived,
        "export_csv",
    ]
    inlines = [
        OrderInline,
        ProductInLine,
    ]
    list_display = "id", "name", "description_short", "price", "discount", "created_by", "created_at", "archived"
    list_display_links = "id", "name"
    ordering = "id", "name"
    search_fields = "name", "description", "price"
    fieldsets = [
        (None, {
           "fields": ("name", "description", "created_by"),
        }),
        (_("Price options"), {
            "fields": ("price", "discount"),
            "classes": ("wide",)
        }),
        (_("Other options"), {
            "fields": ("archived",),
            "classes": ("collapse",),
            "description": "Fields 'archived' is for soft delete",
        }),
        (_("Images"), {
            "fields": ("preview", ),
        }),
    ]

    @admin.display(description=_("description_short"))
    def description_short(self, obj: Product) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + "..."


class ProductInline(admin.TabularInline):
    model = Order.products.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]
    list_display = "id", "delivery_address", "promocode", "created_at", "user_verbouse"

    def get_queryset(self, request):
        return Order.objects.select_related("user").prefetch_related("products")

    @admin.display(description=_("user_verbouse"))
    def user_verbouse(self, obj: Order) -> str:
        return obj.user.first_name or obj.user.username
