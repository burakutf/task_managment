from rest_framework import viewsets
from inupmt_be.account.models import User

from inupmt_be.account.serializers import UserSerializer

# Create your views here.

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


