#accounts / tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from task.models import Team
import logging
from django.test import TestCase


class LoggingTest(TestCase):
    def test_logging(self):
        """
        로깅 메시지를 기록을 확인합니다. 
        """
        logging.debug("This is a debug message")
        logging.info("This is an info message")
        logging.warning("This is a warning message")

        with open("debug.log", "r") as log_file:
            log_contents = log_file.read()

        self.assertIn("This is a debug message", log_contents)
        self.assertIn("This is an info message", log_contents)
        self.assertIn("This is a warning message", log_contents)

User = get_user_model()


class UserModelTest(TestCase):
    def test_create_user(self):
        """
        새로운 사용자 생성이 성공하는지 테스트 입니다.
        """
        username = "testuser"
        password = "testpass123"
        user = User.objects.create_user(
            username=username,
            password=password,
        )

        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))


class UserApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.get(name="단비") 

    def test_create_user_successful(self):
        """
        유효한 데이터로 사용자 생성이 성공하는지 테스트입니다.
        """
        payload = {
            "username": "testuser",
            "password": "testpass123",
            "team": self.team.name,
        }
        res = self.client.post(reverse("signup"), payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(username=payload["username"])
        self.assertTrue(user.check_password(payload["password"]))
        self.assertNotIn("password", res.data)
        self.assertEqual(user.team.name, self.team.name)

    def test_user_exists(self):
        """
        이미 존재하는 사용자를 생성하려 할 때 실패하는지 테스트입니다.
        """
        payload = {"username": "testuser", "password": "testpass123"}
        User.objects.create_user(**payload)

        res = self.client.post(reverse("signup"), payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_for_user(self):
        """
        사용자를 위한 토큰이 생성되는지 테스트입니다.
        """
        payload = {"username": "testuser", "password": "testpass123"}
        User.objects.create_user(**payload)

        res = self.client.post(reverse("token_obtain_pair"), payload)

        self.assertIn("access", res.data)
        self.assertIn("refresh", res.data)

    def test_create_token_invalid_credentials(self):
        """
        잘못된 자격증명으로 토큰이 생성되지 않는지 테스트입니다.
        """
        User.objects.create_user(username="testuser", password="testpass123")
        payload = {"username": "testuser", "password": "wrong"}

        res = self.client.post(reverse("token_obtain_pair"), payload)

        self.assertNotIn("access", res.data)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
