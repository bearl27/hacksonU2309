from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Todo, TodoDay
from .forms import TodoForm
from django.urls import reverse_lazy


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


class TodoUpdate(UpdateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("list")


class TodoDelete(DeleteView):
    model = Todo
    context_object_name = "task"
    success_url = reverse_lazy("list")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


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
