# task / urls.py
from django.urls import path
from .views import (
    TeamListView,
    TaskListView,
    TaskDetailView,
    SubTaskListView,
    SubTaskDetailView,
    TaskCompleteView,
    SubTaskCompleteView,
)

urlpatterns = [
    path("teams/", TeamListView.as_view(), name="team-list"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path(
        "tasks/<int:task_id>/subtasks/", SubTaskListView.as_view(), name="subtask-list"
    ),
    path(
        "tasks/<int:task_id>/subtasks/<int:pk>/", 
        SubTaskDetailView.as_view(),
        name="subtask-detail",
    ),
    path("tasks/<int:pk>/complete/", TaskCompleteView.as_view(), name="task-complete"),
    path(
        "task/<int:task_id>/subtasks/<int:pk>/complete/",
        SubTaskCompleteView.as_view(),
        name="subtask-complete",
    ),
]
