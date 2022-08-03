from rest_framework.viewsets import ModelViewSet
from .models import Users
from .serializers import UsersModelSerializer


class UsersModelViewSet(ModelViewSet):
    serializer_class = UsersModelSerializer
    queryset = Users.objects.all()
