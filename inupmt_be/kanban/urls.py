from django.urls import path
from .views import UsernameAuthView, TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
urlpatterns = [
    path('login/', UsernameAuthView.as_view(), name='login'),
]

router.register(r'tasks', TaskViewSet)

urlpatterns += router.urls