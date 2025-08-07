from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
import pytest


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_returns_401(self, api_client):
        response = api_client.post("/store/collections/", {"title": "a"})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, api_client):
        api_client.force_authenticate(user={})
        response = api_client.post("/store/collections/", {"title": "a"})
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_invalid_data_returns_400(self, api_client):
        api_client.force_authenticate(user=User(is_staff=True))
        response = api_client.post("/store/collections/", {"title": ""})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["title"] == ["This field may not be blank."]

    def test_if_valid_data_returns_201(self, api_client):
        api_client.force_authenticate(user=User(is_staff=True))
        response = api_client.post("/store/collections/", {"title": "a"})
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["id"] > 0
