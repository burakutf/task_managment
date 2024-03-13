from rest_framework import serializers

from account.models import User
from .models import Task, Labels, Comment


class MNUserSerializer(serializers.ModelSerializer):
    avatarUrl = serializers.ImageField(source='avatar')
    id = serializers.CharField()

    class Meta:
        model = User
        fields = (
            'avatarUrl',
            'username',
            'id',
        )


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labels
        fields = ('title',)


class MNCommentSerializer(serializers.ModelSerializer):
    message = serializers.CharField(source='content')
    createdAt = serializers.DateTimeField(source='create_time')
    messageType = serializers.SerializerMethodField()
    name = serializers.CharField(source='author.username')
    id = serializers.CharField()

    class Meta:
        model = Comment
        fields = ('message', 'id', 'createdAt', 'messageType', 'name')

    def get_messageType(self, obj):
        return 'text'


class TimestampField(serializers.Field):
    def to_representation(self, value):
        # Convert the datetime object to a timestamp milliseconds
        return value.timestamp() * 1000


class TaskSerializer(serializers.ModelSerializer):
    assignee = MNUserSerializer(source='assignees', many=True, read_only=True)
    labels = LabelSerializer(many=True, read_only=True)
    start = TimestampField(source='start_time', read_only=True)
    end = TimestampField(source='end_time', read_only=True)
    reporter = MNUserSerializer()
    status = serializers.CharField(source='column.title')
    comments = MNCommentSerializer(
        source='task_comments', many=True, read_only=True
    )
    id = serializers.CharField()
    attachments = serializers.SerializerMethodField()

    class Meta:
        model = Task
        exclude = ('assignees',)

    def get_attachments(self, obj):
        return []

    def create(self, validated_data):
        assignees_data = validated_data.pop('assignees')
        instance = Task.objects.create(**validated_data)
        instance.assignees.set(assignees_data)
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['labels'] = [
            label['title'] for label in representation['labels']
        ]
        representation['due'] = []
        if 'start' in representation:
            representation['due'].append(representation['start'])
        if 'end' in representation:
            representation['due'].append(representation['end'])
        return representation

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
    
    def create(self, validated_data):
        author = self.context['request'].user
        validated_data['author'] = author
        return super().create(validated_data)