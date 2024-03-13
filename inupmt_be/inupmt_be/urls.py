from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from kanban.views import (
    CommentViewSet,
    UsernameAuthView,
    TaskViewSet,
)
from account.views import UserViewSet
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title='API Documentation',
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()

router.register(r'tasks', TaskViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', UsernameAuthView.as_view(), name='login'),
    path(
        'docs/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

urlpatterns += router.urls
