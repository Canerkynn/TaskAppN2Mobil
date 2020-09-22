from django.urls import path, include
from rest_framework import routers

from .views import TaskViewSet, UserViewSet, GorevliViewSet

router = routers.DefaultRouter()
router.register('tasks',TaskViewSet)
router.register('users',UserViewSet)
router.register('gorevli',GorevliViewSet)


urlpatterns = [
    path('',include(router.urls)),
]
