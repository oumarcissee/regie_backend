from django.urls import path, include

from .views import UnitModelViewsets

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', UnitModelViewsets, basename='unites')

urlpatterns = [
    path('', include(router.urls)),
]