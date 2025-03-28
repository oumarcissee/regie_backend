from django.urls import path, include

from .views import OtherSpendModelViewsets

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', OtherSpendModelViewsets, basename='OtherSpends')

urlpatterns = [
    path('', include(router.urls)),
]