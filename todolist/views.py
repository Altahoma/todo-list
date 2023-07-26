from django.views import generic

from .models import Task, Tag


class TaskList(generic.ListView):
    model = Task


class TagList(generic.ListView):
    model = Tag
