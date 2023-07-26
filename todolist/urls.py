from django.urls import path

from .views import TaskList, TaskCreateView, TagList, toggle_task_completion

urlpatterns = [
    path("", TaskList.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/toggle/", toggle_task_completion, name="toggle-task"),
    path("tags/", TagList.as_view(), name="tag-list"),
]

app_name = "todolist"
