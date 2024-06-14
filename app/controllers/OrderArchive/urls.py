from django.urls import path, include

from .views import  OrderArchiveModelViewsets

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', OrderArchiveModelViewsets, basename='orders_archive')

urlpatterns = [
    path('', include(router.urls)),
]