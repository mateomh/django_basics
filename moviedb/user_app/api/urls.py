from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import registration_view

urlpatters = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', registration_view, name='register'),
]