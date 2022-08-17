from rest_framework.viewsets import ModelViewSet
from .models import Projects, TODO
from .serializers import ProjectsModelSerializer, TODOModelSerializer


class ProjectsModelViewSet(ModelViewSet):
    serializer_class = ProjectsModelSerializer
    queryset = Projects.objects.all()


class TODOModelViewSet(ModelViewSet):
    serializer_class = TODOModelSerializer
    queryset = TODO.objects.all()
