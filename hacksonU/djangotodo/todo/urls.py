from . import views
from django.urls import path

urlpatterns = [
    path("", views.TodoList.as_view(), name="list"),
    path('detail/<int:pk>/', views.TodoDetail.as_view(), name='detail') ,
    path('todo_home/', views.TaskListView.as_view(), name='todo_home'),
]
