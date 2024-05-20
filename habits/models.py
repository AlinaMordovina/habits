from django.conf import settings
from django.db import models


class Habit(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    place = models.CharField(max_length=150, verbose_name='Место')
    time = models.TimeField(default='10:00:00', verbose_name='Время')
    action = models.CharField(max_length=100, verbose_name='Действие')
    is_nice_habit = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL,
                                      verbose_name='Cвязанная привычка')
    request_period = models.IntegerField(default=1, blank=True, null=True, verbose_name='Периодичность')
    reward = models.CharField(max_length=250, blank=True, null=True, verbose_name='Вознаграждение')
    duration = models.PositiveIntegerField(blank=True, null=True, verbose_name='Длительность выполнения')
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    def __str__(self):
        return f'{self.owner} в {self.place} делает {self.action} в {self.time}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
