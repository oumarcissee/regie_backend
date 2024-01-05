from django.urls import path, include

urlpatterns = [
    path('app/', include('app.controllers.urls')),
] 


