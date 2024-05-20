from rest_framework import serializers

from habits.models import Habit
from habits.validators import (RelateAndRewardValidator, HabitRelatedAndIsNiceValidator, HabitIsNiceValidator,
                               RequestPeriodHabitValidator, HabitDurationValidator)


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RelateAndRewardValidator(field1='related_habit', field2='reward'),
            HabitRelatedAndIsNiceValidator(field1='related_habit', field2='is_nice_habit'),
            HabitIsNiceValidator(field1='related_habit', field2='reward', field3='is_nice_habit'),
            HabitDurationValidator(field='duration'),
            RequestPeriodHabitValidator(field='request_period'),
        ]
