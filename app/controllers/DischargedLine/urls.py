from django.urls import path, include

from .views import DischargedLinesModelViewsets

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', DischargedLinesModelViewsets, basename='discharge_lines')

urlpatterns = [
    path('', include(router.urls)),
]