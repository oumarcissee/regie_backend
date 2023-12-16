from django.urls import path, include

urlpatterns = [
    path('u/', include('app.controllers.User.urls')),

] 


