# tasks / tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from .models import Team, Task
from django.urls import reverse
import logging
from django.test import TestCase


class LoggingTest(TestCase):
    def test_logging(self):
        """
        로깅 메시지를 기록합니다.
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


class TeamModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 이미 마이그레이션으로 생성된 팀 중 하나를 사용
        cls.team = Team.objects.get(name="단비")

class TaskModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="testuser", password="testpass123")
        cls.team = Team.objects.get(name="단비")
        cls.task = Task.objects.create(
            create_user=cls.user, team=cls.team, title="새 업무", content="업무 내용"
        )

    def test_task_creation(self):
        """
        업무가 올바르게 생성되는지 테스트입니다.
        """
        self.assertEqual(self.task.title, "새 업무")
        self.assertEqual(self.task.content, "업무 내용")
        self.assertFalse(self.task.is_complete)

class TaskViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.team = Team.objects.get(name="단비")
        self.user.team = self.team
        self.user.save()
        
        self.task = Task.objects.create(
            create_user=self.user, team=self.team, title="새 업무", content="업무 내용"
        )
        self.client.force_authenticate(user=self.user)

    def test_task_creation_view(self):
        """
        업무 생성 뷰가 정상 작동하는지 테스트입니다.
        """
        payload = {
            "team": self.team.name,
            "title": "새로운 업무",
            "content": "업무 내용",
            "subtasks_task": [
                {
                    "title": "하위 업무 1",
                    "team": self.team.name
                },
                {
                    "title": "하위 업무 2",
                    "team": self.team.name
                }
            ]
        }
        response = self.client.post(reverse("task-list"), payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_retrieve_task(self):
        """
        업무 목록을 조회하는 뷰가 정상 작동하는지 테스트입니다.
        """
        response = self.client.get(reverse("task-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_task_detail_view(self):
        """
        업무 상세 조회 뷰가 정상 작동하는지 테스트입니다.
        """
        response = self.client.get(reverse("task-detail", kwargs={"pk": self.task.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.task.title)
