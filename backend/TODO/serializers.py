from rest_framework.serializers import ModelSerializer
from .models import Projects, TODO


class ProjectsModelSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class TODOModelSerializer(ModelSerializer):
    # project_name = ProjectsModelSerializer()

    class Meta:
        model = TODO
        # fields = '__all__'
        exclude = ['is_active']
