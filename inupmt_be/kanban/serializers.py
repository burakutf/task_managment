from rest_framework import serializers
from .models import Task, UserModel

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        
    def create(self, validated_data):
        assignees_data = validated_data.pop('assignees')
        instance = Task.objects.create(**validated_data)
        instance.assignees.set(assignees_data)
        return instance
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'