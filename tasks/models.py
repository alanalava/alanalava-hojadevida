from django.db import models

class DatosPersonales(models.Model):
    SEXO_CHOICES = [('H', 'Hombre'), ('M', 'Mujer')]

    idperfil = models.AutoField(primary_key=True)
    descripcionperfil = models.CharField(max_length=50, blank=True, null=True, verbose_name="Descripción del Perfil")
    perfilactivo = models.BooleanField(default=True, verbose_name="¿Perfil Activo?")
    archivo_pdf = models.FileField(upload_to='cv_pdf/', blank=True, null=True, verbose_name="Archivo PDF (Descargable)")

    # === CAMPO NUEVO PARA TU FOTO DE PERFIL ===
    foto_perfil = models.ImageField(upload_to='perfil_fotos/', blank=True, null=True, verbose_name="Foto de Perfil")
    # ==========================================

    apellidos = models.CharField(max_length=60, verbose_name="Apellidos")
    nombres = models.CharField(max_length=60, verbose_name="Nombres")
    nacionalidad = models.CharField(max_length=20, verbose_name="Nacionalidad")
    lugarnacimiento = models.CharField(max_length=60, verbose_name="Lugar de Nacimiento")
    fechanacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    numerocedula = models.CharField(max_length=10, unique=True, verbose_name="Número de Cédula")
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name="Sexo")
    estadocivil = models.CharField(max_length=50, verbose_name="Estado Civil")
    licenciaconducir = models.CharField(max_length=6, blank=True, null=True, verbose_name="Licencia de Conducir")
    telefonoconvencional = models.CharField(max_length=15, blank=True, null=True, verbose_name="Teléfono Convencional")
    telefonofijo = models.CharField(max_length=15, blank=True, null=True, verbose_name="Teléfono Fijo")
    
    email = models.EmailField(max_length=100, blank=True, null=True, verbose_name="Correo Electrónico")

    direcciontrabajo = models.CharField(max_length=50, blank=True, null=True, verbose_name="Dirección Trabajo")
    direcciondomiciliaria = models.CharField(max_length=50, verbose_name="Dirección Domiciliaria")
    sitioweb = models.CharField(max_length=60, blank=True, null=True, verbose_name="Sitio Web")

    def __str__(self): return f"{self.apellidos} {self.nombres}"
    class Meta: verbose_name = "Dato Personal"; verbose_name_plural = "Datos Personales"

class ExperienciaLaboral(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE, related_name='experiencias')
    cargodesempenado = models.CharField(max_length=100, verbose_name="Cargo Desempeñado")
    nombrempresa = models.CharField(max_length=50, verbose_name="Nombre de la Empresa")
    lugarempresa = models.CharField(max_length=50, verbose_name="Lugar de la Empresa")
    fechainiciogestion = models.DateField(verbose_name="Fecha Inicio")
    fechafingestion = models.DateField(blank=True, null=True, verbose_name="Fecha Fin")
    descripcionfunciones = models.CharField(max_length=100, verbose_name="Funciones")
    activarparaqueseveaenfront = models.BooleanField(default=True, verbose_name="Visible en Web")
    rutacertificado = models.FileField(upload_to='certificados/laboral/', blank=True, null=True, verbose_name="Certificado")
    class Meta: verbose_name = "Experiencia Laboral"; verbose_name_plural = "Experiencias Laborales"

class Reconocimientos(models.Model):
    TIPO_CHOICES = [('Académico', 'Académico'), ('Público', 'Público'), ('Privado', 'Privado')]
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE, related_name='reconocimientos')
    tiporeconocimiento = models.CharField(max_length=100, choices=TIPO_CHOICES, verbose_name="Tipo")
    fechareconocimiento = models.DateField(verbose_name="Fecha")
    descripcionreconocimiento = models.CharField(max_length=100, verbose_name="Descripción")
    entidadpatrocinadora = models.CharField(max_length=100, verbose_name="Entidad")
    activarparaqueseveaenfront = models.BooleanField(default=True, verbose_name="Visible en Web")
    rutacertificado = models.FileField(upload_to='certificados/reconocimientos/', blank=True, null=True, verbose_name="Certificado o Evidencia")
    class Meta: verbose_name = "Reconocimiento"; verbose_name_plural = "Reconocimientos"

class CursosRealizados(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE, related_name='cursos')
    nombrecurso = models.CharField(max_length=100, verbose_name="Nombre del Curso")
    fechainicio = models.DateField(verbose_name="Fecha Inicio")
    fechafin = models.DateField(verbose_name="Fecha Fin")
    totalhoras = models.IntegerField(verbose_name="Total Horas")
    descripcioncurso = models.CharField(max_length=100, verbose_name="Descripción")
    entidadpatrocinadora = models.CharField(max_length=100, verbose_name="Entidad")
    activarparaqueseveaenfront = models.BooleanField(default=True, verbose_name="Visible en Web")
    rutacertificado = models.FileField(upload_to='certificados/cursos/', blank=True, null=True, verbose_name="Certificado")
    class Meta: verbose_name = "Curso Realizado"; verbose_name_plural = "Cursos Realizados"

class VentaGarage(models.Model):
    ESTADO_CHOICES = [('Bueno', 'Bueno'), ('Regular', 'Regular')]
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE, related_name='ventas')
    nombreproducto = models.CharField(max_length=100, verbose_name="Nombre Producto")
    estadoproducto = models.CharField(max_length=40, choices=ESTADO_CHOICES, verbose_name="Estado")
    descripcion = models.CharField(max_length=100, verbose_name="Descripción")
    valordelbien = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Precio")
    activarparaqueseveaenfront = models.BooleanField(default=True, verbose_name="Visible en Web")
    imagenproducto = models.ImageField(upload_to='ventas_garage/', blank=True, null=True, verbose_name="Foto del Producto")
    class Meta: verbose_name = "Venta de Garage"; verbose_name_plural = "Ventas de Garage"
    
    # En models.py (al final o junto a los otros modelos)

class HabilidadTecnica(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE, related_name='habilidades')
    nombre_habilidad = models.CharField(max_length=50, verbose_name="Tecnología (ej. Python)")
    porcentaje = models.IntegerField(verbose_name="Porcentaje (0-100)", help_text="Solo números, sin el signo %")

    class Meta:
        verbose_name = "Habilidad Técnica"
        verbose_name_plural = "Habilidades Técnicas"
    
    def __str__(self):
        return f"{self.nombre_habilidad} ({self.porcentaje}%)"