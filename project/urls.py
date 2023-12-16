from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.jwt')),
    
    path('api/', include('app.controllers.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]