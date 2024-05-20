from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.ru', password='5462')
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            place='test_place',
            action='test_action',
            owner=self.user
        )

    def test_create_habit(self):
        url = reverse('habits:habit_create')

        data = {
            'place': 'test_create',
            'action': 'test_create',
            'owner': self.user.pk
        }

        response = self.client.post(url, data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Habit.objects.all().count(), 2)

    def test_list_habit(self):
        url = reverse('habits:habit_list')

        response = self.client.get(url)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results':
                    [
                        {
                            'id': self.habit.id,
                            'place': 'test_place',
                            'time': self.habit.time,
                            'date': self.habit.date,
                            'action': 'test_action',
                            'is_pleasant': self.habit.is_pleasant,
                            'reward': self.habit.reward,
                            'duration': self.habit.duration,
                            'periodicity': self.habit.periodicity,
                            'is_public': self.habit.is_public,
                            'owner': self.user.pk,
                            'related_habit': self.habit.related_habit
                        }
                    ]
            }
        )

    def test_update_habit(self):
        url = reverse('habits:habit_update', args=(self.habit.pk,))
        data = {
            'place': 'place_update',
            'action': 'action_update'
        }
        response = self.client.patch(url, data)
        data = response.json()

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            data,
            {
                'id': self.habit.id,
                'place': 'place_update',
                'time': self.habit.time,
                'date': self.habit.date,
                'action': 'action_update',
                'is_pleasant': self.habit.is_pleasant,
                'reward': self.habit.reward,
                'duration': self.habit.duration,
                'periodicity': self.habit.periodicity,
                'is_public': self.habit.is_public,
                'owner': self.user.pk,
                'related_habit': self.habit.related_habit
            }
        )

    def test_duration_habit(self):
        url = reverse('habits:habit_create')
        data = {
            'place': 'test_place',
            'action': 'test_action',
            'duration': '130',
            'owner': self.user.pk,
        }
        response = self.client.post(url, data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_request_period_habit(self):
        url = reverse('habits:habit_create')
        data = {
            'place': 'test_place',
            'action': 'test_action',
            'request_period': 8,
            'owner': self.user.pk
        }
        response = self.client.post(url, data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_reward_and_is_nice_habit(self):
        url = reverse('habits:habit_create')
        data = {
            'place': 'test_place',
            'action': 'test_action',
            'reward': 'reward_test',
            'owner': self.user.pk,
            'related_habit': 1
        }
        response = self.client.post(url, data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
