from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Users
from .serializers import UsersModelSerializer
from rest_framework import mixins


class UsersModelViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = UsersModelSerializer
    queryset = Users.objects.all()
