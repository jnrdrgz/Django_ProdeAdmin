from django.db import models

class Prode(models.Model):
	nombre = models.CharField(max_length=120)
	participantes = models.ManyToManyField('Participante')

class Participante(models.Model):
	nombre = models.CharField(max_length=120)

class Fecha(models.Model):
	numero = models.PositiveIntegerField()
	prode = models.ForeignKey('Prode', on_delete=models.CASCADE)

class Partido(models.Model):
	local = models.CharField(max_length=120)
	visitante = models.CharField(max_length=120)
	resultado = models.CharField(max_length=10, default=None, blank=True, null=True)
	fecha = models.ForeignKey('Fecha', on_delete=models.CASCADE)

class Pronostico(models.Model):
	resultado = models.CharField(max_length=10, default=None, blank=True, null=True)
	partido = models.ForeignKey('Partido', on_delete=models.CASCADE)
	participante = models.ForeignKey('Participante', on_delete=models.CASCADE)