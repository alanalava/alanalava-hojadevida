from django.db import models

class DatosPersonales(models.Model):
    nombre = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    resumen = models.TextField(blank=True, null=True)
    
    # imagen = models.ImageField(upload_to='perfil/', blank=True, null=True)  <-- APAGAMOS ESTO TEMPORALMENTE
    
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombre