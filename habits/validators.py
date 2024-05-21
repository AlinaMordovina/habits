from rest_framework.serializers import ValidationError


class RelateAndRewardValidator:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        related_habit = dict(value).get(self.field1)
        reward = dict(value).get(self.field2)

        if related_habit and reward:
            raise ValidationError(
                "Нельзя использовать одновременно связанную привычку и вознаграждение"
            )


class HabitRelatedAndIsNiceValidator:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        related_habit = dict(value).get(self.field1)
        is_nice_habit = dict(value).get(self.field2)

        if related_habit and not is_nice_habit:
            raise ValidationError(
                "Связанной привычкой может быть только приятная привычка"
            )


class HabitIsNiceValidator:
    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, value):
        related_habit = dict(value).get(self.field1)
        reward = dict(value).get(self.field2)
        is_nice_habit = dict(value).get(self.field3)

        if is_nice_habit and reward and related_habit:
            raise ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки"
            )


class HabitDurationValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        duration = dict(value).get(self.field)

        if duration and duration > 120:
            raise ValidationError("Выполнение привычки не может превышать 120 секунд")


class RequestPeriodHabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        request_period = dict(value).get(self.field)

        if isinstance(request_period, int) and (
            request_period > 7 or request_period < 1
        ):
            raise ValidationError(
                "Периодичность привычки не может быть больше 7 и меньше 1"
            )
