from django.contrib import admin
# IMPORTANTE: Agregamos HabilidadTecnica a los imports
from .models import DatosPersonales, ExperienciaLaboral, Reconocimientos, CursosRealizados, VentaGarage, HabilidadTecnica

# --- CONFIGURACIÓN DEL INLINE PARA HABILIDADES ---
class HabilidadTecnicaInline(admin.TabularInline):
    model = HabilidadTecnica
    extra = 1  # Muestra una fila vacía lista para llenar
    classes = ('collapse',) # Opcional: hace que se pueda contraer la sección
# -------------------------------------------------

class ExperienciaLaboralInline(admin.TabularInline):
    model = ExperienciaLaboral
    extra = 0
    classes = ('collapse',)

class ReconocimientosInline(admin.TabularInline):
    model = Reconocimientos
    extra = 0
    classes = ('collapse',)

class CursosRealizadosInline(admin.TabularInline):
    model = CursosRealizados
    extra = 0
    classes = ('collapse',)

class VentaGarageInline(admin.TabularInline):
    model = VentaGarage
    extra = 0

@admin.register(DatosPersonales)
class DatosPersonalesAdmin(admin.ModelAdmin):
    list_display = ('apellidos', 'nombres', 'numerocedula', 'perfilactivo')
    
    # AGREGAMOS EL INLINE AQUÍ PARA QUE APAREZCA EN EL ADMIN
    inlines = [
        HabilidadTecnicaInline,   # <--- NUEVO
        ExperienciaLaboralInline, 
        CursosRealizadosInline, 
        ReconocimientosInline, 
        VentaGarageInline
    ]