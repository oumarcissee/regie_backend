from django.urls import path, include

from .views import UserList, UserDetail,UserModelViewsets,ProvidersModelViewsets

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router.register('myusers', UsersModelViewsets, basename='myusers')

urlpatterns = [
   
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('get-users/', UserModelViewsets.as_view({'get': 'list'}), name='getUser'),
    path('get-users/providers/', ProvidersModelViewsets.as_view({'get': 'list'}), name='getProviders'),
    path('', include(router.urls)),
    
]