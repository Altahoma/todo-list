from django.views import generic

from .models import Task, Tag


class TaskList(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"


class TagList(generic.ListView):
    model = Tag
