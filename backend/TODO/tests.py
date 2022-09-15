from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase
from mixer.backend.django import mixer
from .models import Users, Projects
from authapp.views import UsersModelViewSet


class UsersTestCase(TestCase):
    def setUp(self) -> None:
        self.user = Users.objects.create_superuser(username='admin', password='admin')

    def test_get_user_list(self):
        '''
        Тестируем следующий сценарий: запрашиваем список пользователей без аутентификации, получаем 403 код, затем
        логинимся и запрашиваем список еще раз. На выходе получаем словарь с одним пользователем.
        '''
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UsersModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        force_authenticate(request, user=self.user)
        view = UsersModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)


class TODOTestCase(TestCase):
    '''
    Тестирование с использованием APIClient
    '''
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = Users.objects.create_superuser(username='admin', password='admin')

    def test_get_TODO_list(self):
        self.client.force_authenticate(self.user)
        response = self.client.get('/api/TODO/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProjectsTestCase(APITestCase):
    '''
    Тестирование с использованием APITestCase и mixer
    '''
    def setUp(self) -> None:
        self.user = Users.objects.create_superuser(username='admin', password='admin')
        self.project = mixer.cycle(5).blend(Projects)

    def test_get_projects_list(self):
        self.client.force_authenticate(self.user)
        response = self.client.get('/api/Projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 5)
