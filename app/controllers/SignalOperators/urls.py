from django.urls import path, include

from .views import SignalOperatorsModelViewsets

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', SignalOperatorsModelViewsets, basename='signalsOperators')

urlpatterns = [
    path('', include(router.urls)),
]