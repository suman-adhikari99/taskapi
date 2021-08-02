from django.contrib.auth.models import User
from rest_framework import serializers
from .models import  Task, Register

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields = '__all__'

