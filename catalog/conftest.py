import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.fixture
def user():
    return User.objects.create_user(username='test_user_super', password='password_user_super')


@pytest.fixture
def api_client():
    apiclient = APIClient()
    return apiclient