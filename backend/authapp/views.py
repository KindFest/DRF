from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Users
from .serializers import UsersModelSerializer
from rest_framework import mixins
from rest_framework.pagination import LimitOffsetPagination


class UsersLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class UsersModelViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, GenericViewSet):
    pagination_class = UsersLimitOffsetPagination
    serializer_class = UsersModelSerializer
    queryset = Users.objects.all()
