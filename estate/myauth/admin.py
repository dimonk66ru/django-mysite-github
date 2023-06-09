from django.contrib import admin
from .models import Profile
from django.utils.translation import gettext_lazy as _


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = "pk", "profile_name", "bio", "phone", "avatar",

    @admin.display(description=_("profile name"))
    def profile_name(self, obj: Profile) -> str:
        return obj.user.username
