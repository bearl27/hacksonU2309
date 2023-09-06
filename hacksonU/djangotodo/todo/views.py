from django.views.generic import ListView, DetailView
from .models import Task, Todo


class TodoList(ListView):
    model = Todo
    context_object_name = "tasks"

class TodoDetail(DetailView):
    model = Todo
    context_object_name = "task"

class TaskListView(ListView):
    model = Task
    template_name = 'todo/templates/todo/todo_home.html'  # あなたのテンプレート名に合わせて変更
    context_object_name = 'tasks'
