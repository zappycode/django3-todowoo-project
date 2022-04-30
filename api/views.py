from django.utils import timezone
from rest_framework import generics, permissions, response

from . import serializers
from todo.models import Todo


class TodoCompletedList(generics.ListAPIView):
    serializer_class = serializers.TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        todos = Todo.objects.filter(user=user, datecompleted__isnull=False).order_by('-datecompleted')
        return todos


class TodoCreate(generics.ListCreateAPIView):
    serializer_class = serializers.TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        todos = Todo.objects.filter(user=user, datecompleted__isnull=True)
        return todos
    
    def perform_create(self, serializer): 
        serializer.save(user=self.request.user)

class TodoUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
    

class TodoOk(generics.UpdateAPIView):
    serializer_class = serializers.TodoCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.instance.datecompleted = timezone.now()
        serializer.save()
        
    
