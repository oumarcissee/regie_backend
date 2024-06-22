from django.urls import path, include

from .views import  ArchiveModelViewsets

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', ArchiveModelViewsets, basename='archives')

urlpatterns = [
    path('', include(router.urls)),
]