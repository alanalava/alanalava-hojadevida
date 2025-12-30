from django.shortcuts import render
from .models import DatosPersonales

# Función auxiliar para no repetir código
def get_perfil():
    # Busca el perfil activo (1) o devuelve el primero que encuentre
    perfil = DatosPersonales.objects.filter(perfilactivo=1).first()
    if not perfil:
        perfil = DatosPersonales.objects.first()
    return perfil

# --- VISTAS ---
# En todas pasamos 'perfil', y los HTMLs usan perfil.experiencias.all, etc.

def perfil_view(request):
    return render(request, 'perfil.html', {'perfil': get_perfil()})

def perfil_detalle_view(request):
    return render(request, 'perfil_detalle.html', {'perfil': get_perfil()})

def habilidades_view(request):
    return render(request, 'habilidades.html', {'perfil': get_perfil()})

def experiencia_view(request):
    return render(request, 'experiencia.html', {'perfil': get_perfil()})

def educacion_view(request):
    return render(request, 'educacion.html', {'perfil': get_perfil()})

def logros_view(request):
    return render(request, 'logros.html', {'perfil': get_perfil()})

def ventas_view(request):
    return render(request, 'ventas.html', {'perfil': get_perfil()})