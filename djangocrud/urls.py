from django.contrib import admin
from django.urls import path
from tasks import views
from django.conf import settings
from django.conf.urls.static import static

# === AGREGAR ESTE IMPORT ===
from django.contrib.auth import views as auth_views 
# ===========================

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # === RUTAS DE AUTENTICACIÓN (LOGIN / LOGOUT) ===
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    # ===============================================

    path('', views.perfil_view, name='perfil'),
    path('perfil-detalle/', views.perfil_detalle_view, name='perfil_detalle'), 
    path('habilidades/', views.habilidades_view, name='habilidades'),
    path('experiencia/', views.experiencia_view, name='experiencia'),
    path('educacion/', views.educacion_view, name='educacion'),
    path('logros/', views.logros_view, name='logros'),
    path('ventas/', views.ventas_view, name='ventas'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)