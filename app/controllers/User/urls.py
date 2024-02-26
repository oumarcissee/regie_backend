from django.urls import path, include

from .views import CustomUserCreateView, CreateUserProvider

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router.register('myusers', UsersModelViewsets, basename='myusers')

urlpatterns = [
    path('users/', CustomUserCreateView.as_view(), name='custom_user_create'),
    path('create-provider/', CreateUserProvider.as_view(), name='custom_user'),
    path('', include(router.urls)),
    
]