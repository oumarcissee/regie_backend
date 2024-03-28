from django.urls import path, include

from .views import CustomUserCreateView, CreateUserProvider, GetUSerModelViewsets

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router.register('myusers', UsersModelViewsets, basename='myusers')

urlpatterns = [
    path('users/', CustomUserCreateView.as_view(), name='custom_user_create'),
    path('create-provider/', CreateUserProvider.as_view(), name='custom_user'),
    path('get-users/', GetUSerModelViewsets.as_view({'get': 'list'}), name='getUser'),
    path('', include(router.urls)),
    
]