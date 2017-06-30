from django.db import models

class Aparcamiento(models.Model):
    nombre = models.CharField(max_length = 128)
    url = models.URLField() ##
    # CLASE-VIAL, NOMBRE-VIA,NUM, CODIGO-POSTAL,LOCALIDAD, PROVINCIA
    dir2 = models.CharField(max_length = 400)
    # latitud = models.DecimalField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    descripcion = models.TextField()
    accesible = models.BooleanField(default = False)
    barrio = models.CharField(max_length = 64)
    distrito = models.CharField(max_length = 32)
    # <atributo nombre="DATOSCONTACTOS">
    email = models.CharField(max_length = 128, default = "")
    telf = models.CharField(max_length = 64, default = "")
    ncomment = models.IntegerField(default = 0)

class AparcaSeleccionado(models.Model):
    fecha = models.DateField(auto_now_add=True) # (auto_now=True)
    usuario = models.CharField(max_length = 32)
    aparcamiento = models.ForeignKey(Aparcamiento)

class Comentario(models.Model):
    contenido = models.TextField(default="")
    aparcamiento = models.ForeignKey(Aparcamiento)

class Css(models.Model):
    usuario = models.CharField(max_length = 32)#~~RegistradoOK
#    colorLetra = models.CharField(max_length = 32)
#    #tamLetra = models.CharField(max_length=32)
    tamLetra = models.IntegerField()
    colorFondo = models.CharField(max_length = 32)
    titulo = models.CharField(max_length = 128)
