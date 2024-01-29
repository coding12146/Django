# accounts / models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from task.models import Team

class User(AbstractUser):
    """
    사용자 모델
    사용자(User)와 팀(Team) 간의 관계를 정의합니다.
    """
    username = models.CharField(max_length=30, unique=True, verbose_name="아이디")
    team = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="팀명"
    )

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username