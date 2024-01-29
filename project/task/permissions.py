# task / permissions.py
from rest_framework import permissions
from task.models import SubTask, Task

class IsUserInSameTeamAsTask(permissions.BasePermission):
    """
    사용자가 요청한 Task의 팀과 동일한 팀에 속해 있을 때만 접근을 허용합니다.
    """

    def has_permission(self, request, view):
        # SubTaskCompleteView와 TaskCompleteView에서는 `pk`를 사용합니다.
        object_id = view.kwargs.get("pk")
        try:
            # SubTask 또는 Task의 인스턴스를 가져옵니다.
            object_instance = view.get_queryset().get(pk=object_id)
        except (Task.DoesNotExist, SubTask.DoesNotExist):
            return False

        # 사용자의 팀과 Task 또는 SubTask의 팀이 일치할 때만 True를 반환
        return object_instance.team == request.user.team

class IsAuthorOfTask(permissions.BasePermission):
    """
    작성자만 업무(Task)를 수정 및 삭제할 수 있도록 권한을 부여합니다.
    """

    def has_object_permission(self, request, view, obj):
        # 작성자만 수정 및 삭제할 수 있도록 설정
        return obj.create_user == request.user

class IsInDefaultTeam(permissions.BasePermission):
    """
    기본 팀("단비", "다래", "블라블라", "철로", "땅이", "해태", "수피")만 SubTask로 지정할 수 있도록 합니다.
    """

    def has_permission(self, request, view):
        default_teams = ["단비", "다래", "블라블라", "철로", "땅이", "해태", "수피"]

        # Task의 팀 검사
        task_team_name = request.data.get("team")
        if task_team_name not in default_teams:
            return False

        # SubTask의 팀 검사
        subtasks_data = request.data.get("subtasks_task", [])
        for subtask_data in subtasks_data:
            if subtask_data.get("team") not in default_teams:
                return False

        return True