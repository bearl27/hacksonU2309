from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Todo


class TodoList(ListView):
    model = Todo
    context_object_name = "tasks"

class TodoDetail(DetailView):
    model = Todo
    context_object_name = "task"

class ToDoHome(TemplateView):
    template_name = "todo_home.html"
    context_object_name = "home"
