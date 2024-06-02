from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Mova esta linha de volta para o setup/urls.py
    path('', include('apps.galeria.urls')), 
    path('usuarios/', include('apps.usuarios.urls', namespace='usuarios')),  
    path('select2/', include('django_select2.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
