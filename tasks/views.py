from django.shortcuts import render
from .models import DatosPersonales
from django.core.management import call_command
from django.http import HttpResponse

def get_perfil():
    # Solo traemos las tablas que SÍ existen en models.py
    return DatosPersonales.objects.prefetch_related(
        'experiencias', 'reconocimientos', 'cursos', 'ventas'
    ).filter(perfilactivo=True).first()

# --- Tus vistas anteriores ---
def perfil_view(request):
    return render(request, 'perfil.html', {'perfil': get_perfil()})

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

# --- ESTO ES LO QUE DEBES AGREGAR ---
def perfil_detalle_view(request):
    """Vista para mostrar el resumen al tocar la 'A' azul"""
   # Solo trae el primero que encuentres, sin filtros raros
    perfil = DatosPersonales.objects.first()

def reparar_db(request):
    try:
        # 1. Forzar la creación de los planos (migrations)
        call_command('makemigrations', 'tasks')
        # 2. Forzar la construcción de las tablas (migrate)
        call_command('migrate')
        return HttpResponse("<h1>¡ÉXITO! Base de datos reparada.</h1> <p>Ahora intenta entrar al admin.</p>")
    except Exception as e:
        return HttpResponse(f"<h1>ERROR CRÍTICO:</h1> <p>{str(e)}</p>")