from django.urls import path, include

from .views import ItemModelViewsets

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', ItemModelViewsets, basename='signalsOperators.views')

urlpatterns = [
    path('', include(router.urls)),
]