from django.urls import path, include

from .views import OrderModelViewsets

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', OrderModelViewsets, basename='orders')

urlpatterns = [
    path('', include(router.urls)),
]