from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitCreateAPIView, HabitDestroyAPIView,
                          HabitListAPIView, HabitRetrieveAPIView,
                          HabitUpdateAPIView, PublicHabitListAPIView)

app_name = HabitsConfig.name

urlpatterns = [
    path("habits/create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("habits/", HabitListAPIView.as_view(), name="habit_list"),
    path("habits/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit_detail"),
    path("habits/update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("habits/delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="habit_delete"),
    path("public_habits/", PublicHabitListAPIView.as_view(), name="public_habit_list"),
]
