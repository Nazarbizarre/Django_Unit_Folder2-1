import pytest

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient

from accounts.models import Profile

@pytest.mark.django_db
def test_profile_creation():
    user = User.objects.create_user(username='testuser123helloworlds', password='password_test_super')
    # profile = Profile.objects.create(user=user)
    profile = user.profile
    assert profile.avatar == "avatars/logo.jpg"
    assert profile.user == user