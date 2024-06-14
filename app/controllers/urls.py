from django.urls import path, include

urlpatterns = [
    path('u/', include('app.controllers.User.urls')),
    path('items/', include('app.controllers.Item.urls')),
    #La urls de la commande
    path('orders/', include('app.controllers.Order.urls')),
    path('orders-line/', include('app.controllers.OrderLine.urls')),
    path('archives/', include('app.controllers.OrderArchive.urls')),
] 


