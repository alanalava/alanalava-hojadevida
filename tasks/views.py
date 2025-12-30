from django.shortcuts import render
from .models import DatosPersonales
from django.core.management import call_command
from django.http import HttpResponse

def get_perfil():
    # --- CORRECCIÓN CLAVE ---
    # Quitamos .filter(perfilactivo=True) porque ese campo YA NO EXISTE.
    # Quitamos .prefetch_related(...) porque las tablas de experiencias/ventas NO EXISTEN AÚN.
    # Solo traemos el primer dato simple que encuentre.
    return DatosPersonales.objects.first()

# --- Vistas ---
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

def perfil_detalle_view(request):
    # Aquí te faltaba el 'return render', sin eso daba error también
    return render(request, 'perfil_detalle.html', {'perfil': get_perfil()})

# --- REPARADOR DE EMERGENCIA ---
def reparar_db(request):
    try:
        # 1. Forzar la creación de los planos (migrations)
        call_command('makemigrations', 'tasks')
        # 2. Forzar la construcción de las tablas (migrate)
        call_command('migrate')
        return HttpResponse("<h1>¡ÉXITO! Base de datos reparada.</h1> <p>Ahora intenta entrar al admin.</p>")
    except Exception as e:
        return HttpResponse(f"<h1>ERROR CRÍTICO:</h1> <p>{str(e)}</p>")