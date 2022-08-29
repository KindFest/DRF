from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Projects, TODO


class ProjectsModelSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class TODOModelSerializer(ModelSerializer):
    # project_name = StringRelatedField()
    project_name = ProjectsModelSerializer()
    # project_name = project_name['name']

    class Meta:
        model = TODO
        # fields = '__all__'
        exclude = ['is_active']
