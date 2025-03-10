from django.urls import path, include

from .views import DischargeModelViewsets

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', DischargeModelViewsets, basename='discharge_model_viewsets')

urlpatterns = [
    path('', include(router.urls)),
]