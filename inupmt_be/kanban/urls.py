from django.urls import path
from .views import login, TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
urlpatterns = [
    path('login/', login, name='login'),
]

router.register(r'tasks', TaskViewSet)

urlpatterns += router.urls