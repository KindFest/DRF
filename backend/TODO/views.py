from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Projects, TODO
from .serializers import ProjectsModelSerializer, TODOModelSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import mixins


class ProjectsLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class TODOLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectsModelViewSet(ModelViewSet):
    pagination_class = ProjectsLimitOffsetPagination
    serializer_class = ProjectsModelSerializer
    queryset = Projects.objects.all()

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name:
            return Projects.objects.filter(name__contains=name)
        return Projects.objects.all()


class TODOModelViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, GenericViewSet):
    pagination_class = TODOLimitOffsetPagination
    serializer_class = TODOModelSerializer
    queryset = TODO.objects.all()

    def get_queryset(self):
        project_name = self.request.query_params.get('project_name', None)
        if project_name:
            return TODO.objects.filter(project_name=project_name)
        return TODO.objects.all()

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
