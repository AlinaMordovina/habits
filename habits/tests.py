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

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_list_habit(self):
        url = reverse('habits:habit_list')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results':
                    [
                        {
                            'id': self.habit.id,
                            'owner': self.user.pk,
                            'place': 'test_place',
                            'time': self.habit.time,
                            'action': 'test_action',
                            'is_nice_habit': self.habit.is_nice_habit,
                            'related_habit': self.habit.related_habit,
                            'request_period': self.habit.request_period,
                            'reward': self.habit.reward,
                            'duration': self.habit.duration,
                            'is_public': self.habit.is_public,
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

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            data,
            {
                'id': self.habit.id,
                'owner': self.user.pk,
                'place': 'place_update',
                'time': self.habit.time,
                'action': 'action_update',
                'is_nice_habit': self.habit.is_nice_habit,
                'related_habit': self.habit.related_habit,
                'request_period': self.habit.request_period,
                'reward': self.habit.reward,
                'duration': self.habit.duration,
                'is_public': self.habit.is_public,
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

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_request_period_habit(self):
        url = reverse('habits:habit_create')
        data = {
            'place': 'test_place',
            'action': 'test_action',
            'request_period': 8,
            'owner': self.user.pk
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

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

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
