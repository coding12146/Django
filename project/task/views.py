# task / views.py
from rest_framework import generics
from accounts import serializers
from .models import Team, Task, SubTask
from .serializers import (
    SubTaskCompleteSerializer,
    TaskCompleteSerializer,
    TeamSerializer,
    TaskSerializer,
    SubTaskSerializer,
)
from rest_framework.permissions import IsAuthenticated
from .permissions import IsInDefaultTeam, IsUserInSameTeamAsTask, IsAuthorOfTask

class TeamListView(generics.ListAPIView):
    """
    TeamListView: 모든 팀 목록 조회합니다.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TaskListView(generics.ListCreateAPIView):
    """
    TaskListView: 업무(Task) 목록 조회 및 생성합니다.
    """
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAuthenticated]
        return super(TaskListView, self).get_permissions()
    
    def perform_create(self, serializer):
        serializer.save(create_user=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    TaskDetailView: 특정 업무(Task)의 상세 정보 조회, 수정 및 삭제합니다.
    """
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsAuthorOfTask]


class SubTaskListView(generics.ListCreateAPIView):
    """
    SubTaskListView: 특정 업무(Task)의 하위업무(SubTask) 목록 조회 및 생성합니다.
    """
    
    serializer_class = SubTaskSerializer
    permission_classes = [IsAuthenticated, IsUserInSameTeamAsTask]

    # 사용자의 팀과 일치하는 SubTask만 반환합니다.
    def get_queryset(self):
        task_id = self.kwargs.get("task_id")
        return SubTask.objects.filter(task_id=task_id)  

    def perform_create(self, serializer):
        task_id = self.kwargs.get("task_id")
        task = Task.objects.get(pk=task_id)
        serializer.save(task=task)


class SubTaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    SubTaskDetailView: 특정 하위업무(SubTask)의 상세 정보 조회, 수정 및 삭제합니다.
    """
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.is_complete:
            # 완료된 하위업무는 삭제 불가능
            raise serializers.ValidationError("Completed subtasks cannot be deleted.")
        instance.delete()

class SubTaskCompleteView(generics.UpdateAPIView):
    """
    SubTaskCompleteView: 특정 하위업무(SubTask)의 완료 여부 업데이트합니다.
    """
    
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCompleteSerializer
    permission_classes = [IsAuthenticated, IsUserInSameTeamAsTask]  # 수정된 부분

    def perform_update(self, serializer):
        serializer.save()


class TaskCompleteView(generics.UpdateAPIView):
    """
    TaskCompleteView: 특정 업무(Task)의 완료 여부 업데이트합니다.
    """
    
    queryset = Task.objects.all()
    serializer_class = TaskCompleteSerializer
    permission_classes = [IsAuthenticated, IsUserInSameTeamAsTask]  # 수정된 부분

    def perform_update(self, serializer):
        serializer.save()
