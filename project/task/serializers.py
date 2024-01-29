#task / serializers.py
from django.utils import timezone
from rest_framework import serializers
from .models import Team, Task, SubTask
from django.contrib.auth import get_user_model

User = get_user_model()

class TeamSerializer(serializers.ModelSerializer):
    """
    TeamSerializer는 'Team' 모델의 인스턴스를 직렬화/역직렬화하기 위한 클래스입니다.
    이 클래스는 모델의 모든 필드를 포함하는 직렬화 형식을 제공합니다.
    """
    class Meta:
        model = Team
        fields = "__all__"


class SubTaskSerializer(serializers.ModelSerializer):
    """
    SubTaskSerializer는 'SubTask' 모델의 인스턴스를 직렬화/역직렬화하기 위한 클래스입니다.
    이 클래스는 팀 이름과 태스크 제목을 참조 필드로 사용하며, 
    서브태스크의 생성 및 수정 날짜를 포함한 상세 정보를 제공합니다.
    """
    team = serializers.SlugRelatedField(queryset=Team.objects.all(), slug_field="name")
    task = serializers.SlugRelatedField(read_only=True, slug_field="title")  # 변경된 부분

    class Meta:
        model = SubTask
        fields = ("id", "task", "title", "team", "is_complete", "completed_date", "created_at", "modified_at")
        read_only_fields = ("id", "task", "is_complete", "completed_date", "created_at", "modified_at")


class SubTaskCompleteSerializer(serializers.ModelSerializer):
    """
    SubTaskCompleteSerializer는 'Task' 모델에 대한 완료 상태를 업데이트하기 위한 클래스입니다.
    이 클래스는 완료 상태의 변경을 감지하여 관련 처리를 수행합니다.
    """

    class Meta:
        model = Task
        fields = ("id", "is_complete")
        read_only_fields = ("id",)

    def update(self, instance, validated_data):
        is_complete = validated_data.get("is_complete", instance.is_complete)

        if is_complete != instance.is_complete:
            instance.is_complete = is_complete
            if is_complete:
                instance.completed_date = timezone.now()
            else:
                instance.completed_date = None
            instance.save()

        return instance 

class TaskSerializer(serializers.ModelSerializer):
    """
    TaskSerializer는 'Task' 모델의 인스턴스를 직렬화/역직렬화하기 위한 클래스입니다.
    이 클래스는 태스크의 기본 정보뿐만 아니라, 연관된 서브태스크의 정보도 함께 제공합니다.
    태스크 생성과 업데이트를 지원하며, 서브태스크의 생성과 업데이트를 관리합니다.
    """
    team = serializers.SlugRelatedField(slug_field="name", queryset=Team.objects.all())
    subtasks_task = SubTaskSerializer(many=True)
    class Meta:
        model = Task
        fields = (
            "id",
            "team",
            "title",
            "content",
            "is_complete",
            "completed_date",
            "subtasks_task", 
            "create_user",
            "created_at",
            "modified_at"
        )
        read_only_fields = ("is_complete", "completed_date", "create_user", "created_at", "modified_at")

    def create(self, validated_data):      
        subtasks_data = validated_data.pop('subtasks_task', [])
        team_name = validated_data.pop("team")
        team = Team.objects.get(name=team_name)
        validated_data["team"] = team
        task = Task.objects.create(**validated_data)

        # 추가로 제공된 subtasks가 있다면 생성
        for subtask_data in subtasks_data:
            team_name = subtask_data.pop("team")
            team = Team.objects.get(name=team_name)
            SubTask.objects.create(task=task, team=team, **subtask_data)

        return task
    
    def update(self, instance, validated_data):
        subtasks_data = validated_data.pop('subtasks_task', [])

        # Task 인스턴스 업데이트
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # SubTask 인스턴스 업데이트 또는 생성
        subtasks_instances = {subtask.id: subtask for subtask in instance.subtasks_task.all()}
        for subtask_data in subtasks_data:
            subtask_id = subtask_data.get('id', None)
            if subtask_id and subtask_id in subtasks_instances:
                subtask = subtasks_instances[subtask_id]
                for sub_attr, sub_value in subtask_data.items():
                    setattr(subtask, sub_attr, sub_value)
                subtask.save()
            else:
                SubTask.objects.create(task=instance, **subtask_data)

        # 삭제되어야 할 SubTask 인스턴스를 삭제
        for subtask_id, subtask in subtasks_instances.items():
            if subtask_id not in [data.get('id') for data in subtasks_data]:
                subtask.delete()

        return instance
class TaskCompleteSerializer(serializers.ModelSerializer):
    """
    TaskCompleteSerializer는 'Task' 모델에 대한 완료 상태를 업데이트하기 위한 클래스입니다.
    이 클래스는 완료 상태의 변경을 감지하여 관련 처리를 수행합니다.
    """
    class Meta:
        model = Task
        fields = ("id", "is_complete")
        read_only_fields = ("id",)

    def update(self, instance, validated_data):
        is_complete = validated_data.get("is_complete", instance.is_complete)

        if is_complete != instance.is_complete:
            instance.is_complete = is_complete
            if is_complete:
                instance.completed_date = timezone.now()
            else:
                instance.completed_date = None
            instance.save()

        return instance
