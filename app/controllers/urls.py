from django.urls import path, include

urlpatterns = [
    path('u/', include('app.controllers.User.urls')),
    path('items/', include('app.controllers.Item.urls')),
    #La urls de la commande
    path('orders/', include('app.controllers.Order.urls')),
    path('orders-line/', include('app.controllers.OrderLine.urls')),
    path('archives/', include('app.controllers.Archives.urls')),
    
    path('operators/', include('app.controllers.SignalOperators.urls')),
    
    path('unites/', include('app.controllers.Unit.urls')),
    path('subareas/', include('app.controllers.SubArea.urls')),
    
    #La gestion des boredereaux
    path('line-discharges/', include('app.controllers.DischargedLine.urls')),
    path('discharges/', include('app.controllers.Discharge.urls')),
    path('spends/', include('app.controllers.Spend.urls')),
    path('other-spends/', include('app.controllers.OtherSpend.urls')),
] 


