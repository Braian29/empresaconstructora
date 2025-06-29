# LeWorkConstructora/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('about/', include('about.urls')),
    path('services/', include('services.urls')),
    path('projects/', include('projects.urls')),
]

# ***************************************************************
# *** AÑADE ESTE BLOQUE SOLO PARA SERVIR ARCHIVOS ESTÁTICOS ***
# *** Y DE MEDIOS EN MODO DE DESARROLLO (DEBUG = True)      ***
# ***************************************************************
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    # ¡¡¡IMPORTANTE: Asegúrate de que esta línea esté DESCOMENTADA!!!
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # <--- Esta es la línea crucial