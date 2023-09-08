from django.urls import path
from .views import TodoDetail, TodoList, TodoCreate, TaskListView, TodoUpdate, TodoDelete, TodoCalender

urlpatterns = [
    path("", TodoList.as_view(), name="list"),
    path('detail/<int:pk>/', TodoDetail.as_view(), name='detail'),
    path('todo_home/', TaskListView.as_view(), name='todo_home'),
    path('create/', TodoCreate.as_view(), name='create'),
    path('update/<int:pk>/', TodoUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', TodoDelete.as_view(), name='delete'),
    path('todo_calender/', TodoCalender.as_view(), name='calender'),
]
