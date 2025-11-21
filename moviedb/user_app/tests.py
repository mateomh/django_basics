from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

class RegisterTestCase(APITestCase):
    def test_register(self):
        data = {
            "username": "testcase",
            "email": "testcase@example.com",
            "password": "TestPassword123",
            "password2": "TestPassword123"
        }

        resp = self.client.post(reverse('register'), data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)


class LoginLogoutTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='TestPassword123'
        )
    
    def test_login(self):
        data = {
            "username": "testuser",
            "password": "TestPassword123!"
        }

        resp = self.client.post(reverse('login'), data)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        data['password'] = "TestPassword123"
        resp = self.client.post(reverse('login'), data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_logout(self):
        self.token = Token.objects.get(user=self.user)

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        resp = self.client.post(reverse('logout'))

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        
