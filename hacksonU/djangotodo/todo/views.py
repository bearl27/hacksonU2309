from django.views.generic import ListView, DetailView
from .models import Todo


class TodoList(ListView):
    model = Todo
    context_object_name = "tasks"

class TodoDetail(DetailView):
    model = Todo
    context_object_name = "task"

class TaskListView(ListView):
    model = Todo
    template_name = 'todo/templates/todo/todo_home.html'
    context_object_name = 'tasks'
