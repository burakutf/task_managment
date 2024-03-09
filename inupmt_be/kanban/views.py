from rest_framework.views import APIView

from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Task
from .serializers import TaskSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

class UsernameAuthView(APIView):

    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):

        username = request.data.get('username')
        password = request.data.get('password')
        if username is None or password is None:
            return Response({'error': 'Kullanıcı adı ve şifre gereklidir.'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'error': 'Geçersiz kullanıcı adı veya şifre.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
