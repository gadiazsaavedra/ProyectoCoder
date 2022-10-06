from django.db import models

# Create your models here.
"""class familiar1(models.Model):

    nombre = models.CharField (max_length=40)
    apellido = models.CharField (max_length=40)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()

class familiar2(models.Model):

    nombre = models.CharField (max_length=40)
    apellido = models.CharField (max_length=40)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
 
class familiar3(models.Model):

    nombre = models.CharField (max_length=40)
    apellido = models.CharField (max_length=40)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()"""


class Persona(models.Model):

    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    fecha = models.DateField()
