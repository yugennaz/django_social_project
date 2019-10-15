import tempfile

from rest_framework.test import APIClient
import pytest

from django_social_project.models import User, Image, Follower


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def data(db):
    alice = User.objects.create_user(username='alice', password='password')
    bob = User.objects.create_user(username='bob', password='password')
    charlie = User.objects.create_user(username='charlie', password='password')
    david = User.objects.create_user(username='david', password='password')

    Follower.objects.create(follower=alice, following=bob)
    Follower.objects.create(follower=alice, following=david)
    Follower.objects.create(follower=bob, following=alice)
    Follower.objects.create(follower=charlie, following=alice)
    Follower.objects.create(follower=david, following=alice)

    # Создать две картинки для каждого пользователя
    for user in User.objects.all():
        for i in range(2):
            Image.objects.create(
                user=user,
                image=tempfile.NamedTemporaryFile(suffix='.jpg').name,
            )


def test_users_list(data, api_client):
    response = api_client.get('/api/users/')
    assert response.status_code == 200
    response = response.json()
    assert len(response) == len(User.objects.all())


def test_users_detail(data, api_client):
    response = api_client.get('/api/users/1/')
    assert response.status_code == 200
    response = response.json()
    assert response['username'] == 'alice'
    assert len(response['images']) == 2
