from django.contrib import admin
from .models import Estate, EstateType, RoomCount


admin.site.register(EstateType)
admin.site.register(RoomCount)


@admin.register(Estate)
class AuthorAdmin(admin.ModelAdmin):
    list_display = "pk", "seller", "address", "estate_type", "room_count", "price", "created_at"
