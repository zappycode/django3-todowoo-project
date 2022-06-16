from dataclasses import fields
from statistics import mode
from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    datecompleted = serializers.ReadOnlyField()
    
    class Meta:
        model = Todo
        fields = ['id', 'title', 'memo', 'created', 'datecompleted', 'important'] 

# We made this serializers because we don't want the user to change any thing but the state of task being completed
class TodoCompleteSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Todo
        fields = ['id']
        read_only_fields = ['title', 'memo', 'created', 'datecompleted', 'important'] 
