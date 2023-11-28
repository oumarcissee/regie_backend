from django.urls import path, include

from .views import CustomUserCreateView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router.register('myusers', UsersModelViewsets, basename='myusers')

urlpatterns = [
    path('my-users/', CustomUserCreateView.as_view(), name='custom_user_create'),

    path('', include(router.urls)),
    
]