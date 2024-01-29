# task/models.py
import datetime
from django.db import models
from django.conf import settings 
from django.db.models.signals import post_migrate
from django.dispatch import receiver

class Team(models.Model):
    """
    팀(Team) 모델
    팀 정보를 저장하는 모델입니다.

    Attributes:
        name (CharField): 팀명을 저장하는 필드로, 중복을 허용하지 않습니다.

    Methods:
        __str__: 팀 객체를 문자열로 표현합니다.
    """
    name = models.CharField(
        max_length=100, unique=True
    )

    def __str__(self):
        return self.name

# post_migrate 시그널 리시버를 사용하여 초기 팀(Team) 데이터 생성
@receiver(post_migrate)
def create_default_teams(sender, **kwargs):
    if sender.name == 'task':  # 앱 이름이 'task'인 경우에만 초기 데이터 생성
        default_teams = ["단비", "다래", "블라블라", "철로", "땅이", "해태", "수피"]
        for team_name in default_teams:
            Team.objects.get_or_create(name=team_name)

class Task(models.Model):
    """
    업무(Task) 모델
    사용자의 업무 정보를 저장하는 모델입니다.

    Attributes:
        create_user (ForeignKey): 업무를 생성한 사용자와의 관계를 정의합니다.
        team (ForeignKey): 업무가 속한 팀과의 관계를 정의합니다.
        title (CharField): 업무 제목을 저장하는 필드입니다.
        content (TextField): 업무 내용을 저장하는 필드입니다.
        is_complete (BooleanField): 업무의 완료 여부를 나타내는 필드입니다.
        completed_date (DateTimeField): 업무 완료일을 저장하는 필드로, 선택 사항입니다.
        created_at (DateTimeField): 업무 생성일을 저장하는 필드로, 자동으로 현재 시각이 저장됩니다.
        modified_at (DateTimeField): 업무 수정일을 저장하는 필드로, 자동으로 현재 시각이 저장됩니다.

    Methods:
        __str__: 업무 객체를 문자열로 표현합니다.
        save: 업무 객체를 저장할 때 호출되는 메서드로, 추가 동작을 수행합니다.
    """
    create_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_complete = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title  # Task의 제목을 문자열로 반환

    def save(self, *args, **kwargs):
        if self.is_complete and not self.completed_date:
            self.completed_date = datetime.datetime.now()
        elif not self.is_complete and self.completed_date:
            self.completed_date = None

        # Task 객체가 이미 데이터베이스에 저장되었는지 확인
        if self.id is None:
            # Task 객체가 저장되지 않았다면 SubTask 생성
            super(Task, self).save(*args, **kwargs)  # Task 저장
            SubTask.objects.create(task=self, team=self.team, title="업무주관팀")
        else:
            # Task 객체가 이미 저장되었다면 Task 저장만 수행
            super(Task, self).save(*args, **kwargs)

# 하위업무(SubTask) 모델 정의
class SubTask(models.Model):
    """
    하위업무(SubTask) 모델
    업무(Task)의 하위업무 정보를 저장하는 모델입니다.

    Attributes:
        team (ForeignKey): 하위업무가 속한 팀과의 관계를 정의합니다.
        task (ForeignKey): 하위업무가 속한 업무(Task)와의 관계를 정의합니다.
        title (CharField): 하위업무 제목을 저장하는 필드입니다.
        is_complete (BooleanField): 하위업무의 완료 여부를 나타내는 필드입니다.
        completed_date (DateTimeField): 하위업무 완료일을 저장하는 필드로, 선택 사항입니다.
        created_at (DateTimeField): 하위업무 생성일을 저장하는 필드로, 자동으로 현재 시각이 저장됩니다.
        modified_at (DateTimeField): 하위업무 수정일을 저장하는 필드로, 자동으로 현재 시각이 저장됩니다.

    Methods:
        __str__: 하위업무 객체를 문자열로 표현합니다.
        save: 하위업무 객체를 저장할 때 호출되는 메서드로, 추가 동작을 수행합니다.
    """
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="subtasks_team"
    )
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name="subtasks_task"
    )
    title = models.CharField(max_length=200)
    is_complete = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task.title 

    def save(self, *args, **kwargs):
        if self.is_complete and not self.completed_date:
            self.completed_date = datetime.datetime.now()

        elif not self.is_complete and self.completed_date:
            self.completed_date = None

        super(SubTask, self).save(*args, **kwargs)

        if self.task.subtasks_task.filter(is_complete=False).count() == 0:
            self.task.is_complete = True
            self.task.completed_date = datetime.datetime.now()  # 수정된 부분
            self.task.save()
        else:
            self.task.is_complete = False
            self.task.completed_date = None
            self.task.save()