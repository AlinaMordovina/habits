# Generated by Django 5.0.6 on 2024-05-20 17:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("place", models.CharField(max_length=150, verbose_name="Место")),
                ("time", models.TimeField(default="10:00:00", verbose_name="Время")),
                ("action", models.CharField(max_length=100, verbose_name="Действие")),
                (
                    "is_nice_habit",
                    models.BooleanField(
                        default=False, verbose_name="Признак приятной привычки"
                    ),
                ),
                (
                    "request_period",
                    models.IntegerField(
                        blank=True, default=1, null=True, verbose_name="Периодичность"
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="Вознаграждение",
                    ),
                ),
                (
                    "duration",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="Длительность выполнения"
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        default=False, verbose_name="Признак публичности"
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="habits.habit",
                        verbose_name="Cвязанная привычка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
    ]
