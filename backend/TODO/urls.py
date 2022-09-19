from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProjectsModelViewSet, TODOModelViewSet

app_name = 'TODO'

router = DefaultRouter()
router.register('Projects', ProjectsModelViewSet)
router.register('TODO', TODOModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]