from rest_framework import generics, permissions

from . import serializers
from todo.models import Todo


class TodoCompletedList(generics.ListAPIView):
    serializer_class = serializers.TodoSerializer
    queryset = Todo.objects.all()
    permission_class = [permissions.IsAuthenticated]
    
