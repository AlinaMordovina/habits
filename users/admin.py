from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "phone", "tg_id")
    search_fields = (
        "email",
        "phone",
        "tg_id",
    )
