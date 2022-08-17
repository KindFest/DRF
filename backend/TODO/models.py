from django.db import models
from authapp.models import Users
# import authapp.models


class Projects(models.Model):
    name = models.CharField(max_length=256)
    repo_link = models.URLField(max_length=126, null=True)
    users = models.ManyToManyField(Users)

    def __str__(self):
        return f'{self.name}'


class TODO(models.Model):
    project_name = models.ForeignKey(Projects, on_delete=models.CASCADE)
    description = models.CharField(max_length=2048)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    create_by = models.ManyToManyField(Users)
    is_active = models.BooleanField(default=True)
