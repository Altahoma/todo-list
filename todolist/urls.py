from django.urls import path

from .views import (
    TaskList,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    toggle_task_completion,
    TagList,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", TaskList.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"
    ),
    path(
        "task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"
    ),
    path("task/<int:pk>/toggle/", toggle_task_completion, name="toggle-task"),
    path("tags/", TagList.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todolist"
