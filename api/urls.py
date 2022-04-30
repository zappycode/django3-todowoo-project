from django.urls import path

from . import views

urlpatterns = [
    path('completed/', views.TodoCompletedList.as_view(), name='todo-completed'),
]
