from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Todo
from django.urls import reverse_lazy
from django.views import generic
from . import mixins


class TodoList(ListView):
    model = Todo
    context_object_name = "tasks"


class TodoDetail(DetailView):
    model = Todo
    context_object_name = "task"


class TaskListView(ListView, mixins.MonthCalendarMixin):
    model = Todo
    template_name = 'todo/todo_home.html'
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context


class TodoCreate(CreateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("list")


class TodoUpdate(UpdateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("list")


class TodoDelete(DeleteView):
    model = Todo
    context_object_name = "task"
    success_url = reverse_lazy("list")


class TodoCalender(ListView, mixins.MonthCalendarMixin):
    model = Todo
    template_name = 'todo/todo_calender.html'
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context


class TodoCategory(ListView):
    model = Todo
    template_name = 'todo/todo_category.html'
    context_object_name = "tasks"
