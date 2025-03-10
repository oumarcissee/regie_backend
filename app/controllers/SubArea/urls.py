from django.urls import path, include

from .views import SubAreaModelViewsets

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', SubAreaModelViewsets, basename='subarea')

urlpatterns = [
    path('', include(router.urls)),
]