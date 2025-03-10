from django.urls import path, include

from .views import SpendModelViewsets

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', SpendModelViewsets, basename='Spends')

urlpatterns = [
    path('', include(router.urls)),
]