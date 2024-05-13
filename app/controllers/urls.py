from django.urls import path, include

urlpatterns = [
    path('u/', include('app.controllers.User.urls')),
    path('items/', include('app.controllers.Item.urls')),
    path('orders/', include('app.controllers.Order.urls')),
] 


