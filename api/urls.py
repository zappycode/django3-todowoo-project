from django.urls import path

from . import views

urlpatterns = [
    path('todos/', views.TodoCreate.as_view(), name='todo-create'),
    path('todos/<int:pk>', views.TodoUpdate.as_view(), name='todo-create'),
    path('completed/', views.TodoCompletedList.as_view(), name='todo-completed'),
]
