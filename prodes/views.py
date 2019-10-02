from django.shortcuts import render
from prodes.models import Prode, Participante, Fecha
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