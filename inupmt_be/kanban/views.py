from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import Task,Column
from rest_framework.authtoken.models import Token
from .serializers import TaskSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

class UsernameAuthView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        if username is None or password is None:
            return Response(
                {'error': 'Kullanıcı adı ve şifre gereklidir.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = authenticate(username=username, password=password)
        if user is None:
            return Response(
                {'error': 'Geçersiz kullanıcı adı veya şifre.'},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        serialized_data = TaskSerializer(tasks, many=True).data

        custom_response = {
            "board": {
                "columns": {}
            },
            "tasks": {}
        }

        for task_data in serialized_data:
            task_id = task_data['id']
            column_id = task_data['column']
            column = get_object_or_404(Column, pk=column_id) 
            column_name = column.title 
            if column_name not in custom_response['board']['columns']:
                custom_response['board']['columns'][column_name] = {
                    "id": f"{column_name.lower().replace(' ', '-')}-column",
                    "name": column_name,
                    "taskIds": []
                }
            custom_response['board']['columns'][column_name]['taskIds'].append(task_id)
            custom_response['tasks'][task_id] = task_data

        return JsonResponse(custom_response)