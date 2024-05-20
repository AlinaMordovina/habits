from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ("id", "owner", "action", "is_nice_habit", "related_habit", "reward", "is_public")
    list_filter = ("is_nice_habit", "is_public",)
    search_fields = (
        "action",
    )
