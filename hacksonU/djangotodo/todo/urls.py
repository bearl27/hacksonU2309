from django.urls import path
from . import views

urlpatterns = [
    path("", views.TodoList.as_view(), name="list"),
    path("detail/<int:pk>", views.TodoDetail.as_view(), name="detail"),
    path('todo-home/', views.ToDoHome.as_view(), name='todo_home'),
]
