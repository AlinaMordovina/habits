from datetime import date, datetime, timedelta

from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_reminder_about_habit():
    time_now = datetime.now().time().replace(second=0, microsecond=0)
    date_now = date.today()
    habits_list_to_send = Habit.objects.filter(is_nice_habit=False)

    for habit in habits_list_to_send:
        chat_id = habit.owner.tg_id
        if habit.next_message_date == date_now or not habit.next_message_date:
            if habit.time >= time_now and chat_id is not None:
                message = f"Время полезной привычки!) Задание: {habit.action} в {habit.place} и получи {habit.reward}!"
                send_telegram_message(chat_id, message)
                habit.date = date_now + timedelta(days=habit.request_period)
                habit.save()
