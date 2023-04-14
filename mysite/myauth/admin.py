from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = "pk", "profile_name", "bio", "avatar",

    def profile_name(self, obj: Profile) -> str:
        return obj.user.username
