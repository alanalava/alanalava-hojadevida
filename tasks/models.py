from django.db import models

class DatosPersonales(models.Model):
    idperfil = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    profesion = models.CharField(max_length=100, help_text="Ej: Ingeniero en Sistemas")
    descripcionperfil = models.TextField(max_length=500)
    
    fotoperfil = models.ImageField(upload_to='perfil/', null=True, blank=True)
    archivocv = models.FileField(upload_to='cv/', null=True, blank=True)
    
    email_contacto = models.EmailField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direcciondomiciliaria = models.CharField(max_length=100)
    
    perfilactivo = models.IntegerField(default=1) 
    
    # Otros datos
    nacionalidad = models.CharField(max_length=20)
    lugarnacimiento = models.CharField(max_length=60)
    fechanacimiento = models.DateField()
    numerocedula = models.CharField(max_length=10, unique=True)
    sexo_choices = [('H', 'Hombre'), ('M', 'Mujer')]
    sexo = models.CharField(max_length=1, choices=sexo_choices)
    estadocivil = models.CharField(max_length=50)
    sitioweb = models.URLField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    class Meta:
        verbose_name_plural = "Datos Personales"

# --- TABLAS RELACIONADAS ---

class ExperienciaLaboral(models.Model):
    idperfilconqueestaactivo = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE, related_name='experiencias')
    cargodesempenado = models.CharField(max_length=100)
    nombrempresa = models.CharField(max_length=50)
    fechainiciogestion = models.DateField()
    fechafingestion = models.DateField(blank=True, null=True)
    descripcionfunciones = models.TextField(max_length=500)
    activarparaqueseveaenfront = models.BooleanField(default=True)
    rutacertificado = models.FileField(upload_to='certificados/experiencia/', blank=True, null=True)

    def __str__(self):
        return f"{self.cargodesempenado} en {self.nombrempresa}"

class Reconocimientos(models.Model):
    idperfilconqueestaactivo = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE, related_name='reconocimientos')
    tiporeconocimiento = models.CharField(max_length=100)
    fechareconocimiento = models.DateField()
    descripcionreconocimiento = models.CharField(max_length=100)
    entidadpatrocinadora = models.CharField(max_length=100)
    activarparaqueseveaenfront = models.BooleanField(default=True)
    rutacertificado = models.FileField(upload_to='reconocimientos/', null=True, blank=True)

    def __str__(self):
        return self.descripcionreconocimiento

class CursosRealizados(models.Model):
    idperfilconqueestaactivo = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE, related_name='cursos')
    nombrecurso = models.CharField(max_length=100)
    fechainicio = models.DateField()
    fechafin = models.DateField()
    totalhoras = models.IntegerField()
    descripcioncurso = models.CharField(max_length=100)
    entidadpatrocinadora = models.CharField(max_length=100)
    activarparaqueseveaenfront = models.BooleanField(default=True)
    rutacertificado = models.FileField(upload_to='certificados/cursos/', blank=True, null=True)

    def __str__(self):
        return self.nombrecurso

class VentaGarage(models.Model):
    idperfilconqueestaactivo = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE, related_name='ventas')
    nombreproducto = models.CharField(max_length=100)
    estadoproducto = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=100)
    valordelbien = models.DecimalField(max_digits=5, decimal_places=2)
    activarparaqueseveaenfront = models.BooleanField(default=True)
    # Cambiamos el nombre para que coincida con tu HTML viejo si quieres, o usamos este nuevo
    documento_interes = models.FileField(upload_to='garage/', null=True, blank=True) 

    def __str__(self):
        return self.nombreproducto

# Agregué esta tabla que faltaba en el zip para que 'habilidades.html' no falle
class Habilidades(models.Model):
    idperfilconqueestaactivo = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE, related_name='habilidades')
    nombre_habilidad = models.CharField(max_length=100)
    porcentaje = models.IntegerField(help_text="De 0 a 100")

    def __str__(self):
        return self.nombre_habilidad