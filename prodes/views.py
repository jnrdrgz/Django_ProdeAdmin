from django.shortcuts import render
from prodes.models import *
from prodes.forms import NuevoProdeForm, NuevoParticipanteForm

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

def agregar_prode(request):
	form = NuevoProdeForm()
	if request.method == "POST":
		form = NuevoProdeForm(request.POST)
		if form.is_valid():
			prode = Prode(
				nombre = form.cleaned_data["nombre"]
			)

			prode.save()

			prodes = Prode.objects.all()
			context = {
				'prodes': prodes
			}

			return render(request, "prodes.html", context)

	context = {
		"form": form,
	}
	return render(request, "agregar_prode.html", context)

def agregar_participante(request, pk):
	form = NuevoParticipanteForm()
	prode = Prode.objects.get(pk=pk)
		
	if request.method == "POST":	
		form = NuevoParticipanteForm(request.POST)
		if form.is_valid():
			participante = Participante(
				nombre = form.cleaned_data["nombre"],
			)


			participante.save()
			prode.participantes.add(participante)
			prode.save()

			context = {
				'prode': prode
			}

			return render(request, "prode_menu.html", context)

	context = {
		"prode": prode,
		"form": form,
	}

	return render(request, "agregar_participante.html", context)

def fecha(request, prode_pk, fecha_pk):
	prode = Prode.objects.get(pk=prode_pk)
	fecha = Fecha.objects.get(pk=fecha_pk)
	
	context = {
		"prode": prode,
		"fecha": fecha,
	}
	return render(request, "fecha.html", context)

def fecha_partidos(request, prode_pk, fecha_pk):
	prode = Prode.objects.get(pk=prode_pk)
	fecha = Fecha.objects.get(pk=fecha_pk)
	partidos = Partido.objects.filter(fecha=fecha)

	context = {
		"prode": prode,
		"fecha": fecha,
		"partidos": partidos
	}

	return render(request, "fecha_partidos.html", context)

def fecha_tabla(request, prode_pk, fecha_pk):
	pass
	#return render(request, "fecha_tabla.html", context)

