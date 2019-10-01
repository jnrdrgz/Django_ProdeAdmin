from django.db import models

# Create your models here.

class Prode(models.Model):
	nombre = models.CharField(max_length=120)
	participantes = models.ManyToManyField('Participante')

class Participante(models.Model):
	nombre = models.CharField(max_length=120)

class Fecha(models.Model):
	numero = models.PositiveIntegerField()
	prode = models.ForeignKey('Prode', on_delete=models.CASCADE)

#class Partido(models.Model):
#	local = models.CharField(max_length=120)
#	visitante = models.CharField(max_length=120)


	
