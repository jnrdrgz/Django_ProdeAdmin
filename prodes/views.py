from django.shortcuts import render
from prodes.models import Prode, Participante, Fecha
# Create your views here.

def prodes(request):
	prodes = Prode.objects.all()
	context = {
		'prodes': prodes
	}
	return render(request, "prodes.html", context)

def prode_menu(request, pk):
	prode = Prode.objects.get(pk=pk)
	context = {
		'prode': prode
	}

	return render(request, "prode_menu.html", context)

def participantes_menu(request, pk):
	prode = Prode.objects.get(pk=pk)
	participantes = prode.participantes.all()
	context = {
		'prode': prode,
		'participantes': participantes
	}
	
	return render(request, "participantes_menu.html", context)

def fechas_menu(request, pk):
	prode = Prode.objects.get(pk=pk)
	fechas = Fecha.objects.filter(prode=prode)
	context = {
		'prode': prode,
		'fechas': fechas
	}
	
	return render(request, "fechas_menu.html", context)