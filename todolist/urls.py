from django.urls import path

from .views import TaskList, TaskCreateView, TagList


urlpatterns = [
    path("", TaskList.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagList.as_view(), name="tag-list"),
]

app_name = "todolist"
