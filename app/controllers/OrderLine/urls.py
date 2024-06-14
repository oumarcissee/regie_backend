from django.urls import path, include

from .views import OrderLineModelViewsets

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', OrderLineModelViewsets, basename='orders-line')

urlpatterns = [
    path('', include(router.urls)),
]