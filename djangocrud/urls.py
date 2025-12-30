from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.perfil_view, name='perfil'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('detalle/', views.perfil_detalle_view, name='perfil_detalle'), # La "A" azul
    path('habilidades/', views.habilidades_view, name='habilidades'),
    path('experiencia/', views.experiencia_view, name='experiencia'),
    path('educacion/', views.educacion_view, name='educacion'),
    path('logros/', views.logros_view, name='logros'),
    path('ventas/', views.ventas_view, name='ventas'),
]

# Esto permite ver las fotos en modo DEBUG (tu PC)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)