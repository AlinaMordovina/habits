from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(
        max_length=35, blank=True, null=True, verbose_name="Телефон"
    )
    tg_id = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Телеграм id"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
