from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UsersModelViewSet

app_name = 'authapp'

router = DefaultRouter()
router.register('users', UsersModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]