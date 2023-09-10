from django.urls import path
from .views import TodoDetail, TodoList, TodoCreate, TaskListView, TodoUpdate, TodoDelete, TodoCalender, TodoCategory

urlpatterns = [
    path("", views.todo_list, name="list"),
    path('detail/<int:pk>/', TodoDetail.as_view(), name='detail'),
    path('todo_home/', TaskListView.as_view(), name='todo_home'),
    path('update/<int:pk>/', TodoUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', TodoDelete.as_view(), name='delete'),
    path('todo_category/', TodoCategory.as_view(), name='category'),
    path('todo_calender/', TodoCalender.as_view(), name='calender'),
    path('todo_category/', TodoCategory.as_view(), name='category'),
]
