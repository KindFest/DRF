from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Users
from .serializers import UsersModelSerializer, UsersModelSerializerV2
from rest_framework import mixins
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser, \
    BasePermission, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly


class UsersLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class UsersModelViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, GenericViewSet):
    pagination_class = UsersLimitOffsetPagination
    permission_classes = [DjangoModelPermissions]
    # serializer_class = UsersModelSerializer
    queryset = Users.objects.all()

    def get_serializer_class(self):
        if self.request.version == '2.0':
            return UsersModelSerializerV2
        return UsersModelSerializer
