from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from watchlist_app.api import serializers
from watchlist_app import models

class StreamPlatformTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='TestPassword123'
        )
        # self.token = Token.objects.get(user=self.user)
        # self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        self.stream_platform = models.StreamPlatform.objects.create(
            name= "Netflix",
            about= "the best test stream platform",
            url= "https://netflix.com"
        )

    def test_streamplatform_create(self):
        data = {
            "name": "Netflix",
            "about": "the best test stream platform",
            "website": "https://netflix.com"
        }

        resp = self.client.post(reverse('stream-platform-list'), data)

        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_streamplatform_list(self):
        resp = self.client.get(reverse('stream-platform-list'))

        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_streamplatform_show_one(self):
        resp = self.client.get(reverse('stream-platform-detail', args=(self.stream_platform.id,)))

        self.assertEqual(resp.status_code, status.HTTP_200_OK)


class MoviesTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='TestPassword123'
        )
        # self.token = Token.objects.get(user=self.user)
        # self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        self.stream_platform = models.StreamPlatform.objects.create(
            name= "Netflix",
            about= "the best test stream platform",
            url= "https://netflix.com"
        )

        self.movie = models.Movie.objects.create(
            platform=self.stream_platform,
            name= "Original Test movie",
            active= True,
            description= "This is the first test movie"
        )

    def test_movie_create(self):
        data = {
            "platform": self.stream_platform,
            "name": "Test Movie",
            "active": True,
            "description": "A movie to test"
        }

        resp = self.client.post(reverse('movie-list'), data)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_movie_list(self):
        resp = self.client.get(reverse('movie-list'))

        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_movie_get_one(self):
        resp = self.client.get(reverse('movie-detail', args=(self.movie.id,)))

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
