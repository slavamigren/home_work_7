from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Lesson, Course, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        """Заполняем БД перед началом тестов"""
        # новый пользователь, заводить нужно только так, т.к. пароль шифруется
        # и просто созданный через create объект User не сможет авторизоваться
        userdata = {
            'email': 'test@test.ru',
            'password': '12345',
            'role': 'MEMBER'
        }
        # создаём пользователя
        self.client.post(
            '/users/',
            userdata
        )
        # получаем токен
        response = self.client.post(
            '/users/token/',
            userdata
        )
        # добавляем токен к авторизации
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.json().get('access'))

    def test_lesson_create(self):
        """Тест создания урока"""
        data = {
            'title': 'Test',
            'description': 'Test',
        }

        response = self.client.post(
            reverse('lms:lesson_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_lesson_delete(self):
        """Тест удаления урока"""
        # сначала добавляем
        self.lesson = Lesson.objects.create(title='Test', description='Test',
                                            owner=User.objects.get(email='test@test.ru'))
        # теперь удаляем
        response = self.client.delete(
            reverse('lms:lesson_delete', kwargs={'pk': self.lesson.pk}),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_lesson_detail(self):
        """Тест получения одного объекта модели Lesson"""
        # сначала добавляем
        self.lesson = Lesson.objects.create(title='Test', description='Test',
                                            owner=User.objects.get(email='test@test.ru'))
        # теперь получаем
        response = self.client.get(
            reverse('lms:lesson_detail', kwargs={'pk': self.lesson.pk}),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_lesson_list(self):
        """Тест получения всех объектов модели Lesson"""
        # сначала добавляем
        self.lesson = Lesson.objects.create(title='Test', description='Test',
                                            owner=User.objects.get(email='test@test.ru'))
        # теперь получаем
        response = self.client.get(
            reverse('lms:lesson_list'),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_lesson_update(self):
        """Тест обновления"""
        # сначала добавляем
        self.lesson = Lesson.objects.create(title='Test', description='Test',
                                            owner=User.objects.get(email='test@test.ru'))
        # теперь обновляем
        data = {
            'title': 'Test2'
        }

        response = self.client.patch(
            reverse('lms:lesson_update', kwargs={'pk': self.lesson.pk}),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        """Заполняем БД перед началом тестов"""
        # новый пользователь
        userdata = {
            'email': 'test2@test.ru',
            'password': '12345',
            'role': 'STUDENT'
        }
        # создаём пользователя
        response = self.client.post(
            '/users/',
            userdata
        )
        # получаем токен
        response = self.client.post(
            '/users/token/',
            userdata
        )
        # добавляем токен к авторизации
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.json().get('access'))
        # добавляем один курс
        self.course = Course.objects.create(title='Test')

    def test_subscription_create(self):
        """Тест создания подписки"""
        subscription_data = {
            'course': self.course.pk,
        }

        response = self.client.post(
            reverse('lms:subscription_create'),
            data=subscription_data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_subscription_delete(self):
        """Тест удаления подписки"""
        # сначала добавляем подписку
        self.subscription = Subscription.objects.create(course=self.course, user=User.objects.get(email='test2@test.ru'))
        # теперь удаляем
        response = self.client.delete(
            reverse('lms:subscription_delete', kwargs={'pk': self.subscription.pk}),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_subscription_list(self):
        """Тест получения подписок"""
        # сначала добавляем подписку
        self.subscription = Subscription.objects.create(course=self.course, user=User.objects.get(email='test2@test.ru'))
        # теперь получаем
        response = self.client.get(
            reverse('lms:subscription_list'),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
