import operator
from django.shortcuts import render, redirect
from prodes.models import *
from prodes.forms import *



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
	fechas = Fecha.objects.filter(prode=prode).order_by("numero")
	context = {
		'prode': prode,
		'fechas': fechas
	}
	
	return render(request, "fechas_menu.html", context)

def agregar_fecha(request, pk):
	prode = Prode.objects.get(pk=pk)
	fechas = Fecha.objects.filter(prode=prode)
	form = NuevaFechaForm()
	
	if request.method == "POST":
		form = NuevaFechaForm(request.POST)
		if form.is_valid():
			fecha = Fecha(
				numero = form.cleaned_data["numero"],
				prode = prode
			)

			fecha.save()

			return fechas_menu(request, pk)

	context = {
		"prode": prode,
		"form": form,
	}
	return render(request, "agregar_fecha.html", context)

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

def agregar_partido(request, prode_pk, fecha_pk):
	form = NuevoPartidoForm()
	prode = Prode.objects.get(pk=prode_pk)
	fecha = Fecha.objects.get(pk=fecha_pk)
	partidos = Partido.objects.filter(fecha=fecha)

	if request.method == "POST":	
		form = NuevoPartidoForm(request.POST)
		if form.is_valid():
			partido = Partido(
				local=form.cleaned_data["local"],
				visitante=form.cleaned_data["visitante"],
				resultado=form.cleaned_data["resultado"],
				fecha=fecha
			)
			
			partido.save()	

	context = {
		"prode": prode,
		"fecha": fecha,
		"form": form,
		"partidos": partidos
	}				
	return render(request, "agregar_partido.html", context)

def participante(request, prode_pk, participante_pk):
	prode = Prode.objects.get(pk=prode_pk)
	participante = Participante.objects.get(pk=participante_pk)
	context = {
		"prode": prode,
		"participante": participante,
	}

	return render(request, "participante.html", context)

def pronosticos_menu(request, prode_pk, participante_pk):
	prode = Prode.objects.get(pk=prode_pk)
	fechas = Fecha.objects.filter(prode=prode).order_by("numero")
	participante = Participante.objects.get(pk=participante_pk)
	context = {
		'prode': prode,
		'fechas': fechas,
		'participante': participante,
	}
	
	return render(request, "pronosticos_menu.html", context)


def pronosticos(request, prode_pk, participante_pk, fecha_pk):
	prode = Prode.objects.get(pk=prode_pk)
	participante = Participante.objects.get(pk=participante_pk)
	fecha = Fecha.objects.get(pk=fecha_pk)
	partidos = Partido.objects.filter(fecha=fecha)
	pronosticos = Pronostico.objects.filter(participante=participante,partido__in=partidos)

	'''_pron = []
	for pa in partidos:
		for pr in pronosticos:
			if pa == pr.partido:
				_pron.append(pr)
				continue
		_pron.append(None)

	partido_pronostico = dict(zip(partidos, _pron))
	print(partido_pronostico)'''
	#partido_pronostico = dict(itertools.zip_longest(partidos, pronosticos))
	_pron = {}
	for pa in partidos:
		for pr in pronosticos:
			if pa == pr.partido:
				_pron[pa] = pr
				break
		if not pa in _pron.keys():
			_pron[pa] = None

	for k,v in _pron.items():
		if(v):
			print("{} - {} apues: {} real: {}"
			.format(k.local, k.visitante, v.resultado, k.resultado))
		else:
			print("{} - {} apues: {} real: {}"
			.format(k.local, k.visitante, "-", k.resultado))
	partido_pronostico = _pron

	context = {
		"prode": prode,
		"participante": participante,
		"partidos": partidos,
		"pronosticos": pronosticos,
		"pp": partido_pronostico
	}

	return render(request, "pronosticos.html", context)

def editar_pronosticos(request, prode_pk, participante_pk, fecha_pk, pronostico_pk):
	prode = Prode.objects.get(pk=prode_pk)
	participante = Participante.objects.get(pk=participante_pk)
	fecha = Fecha.objects.get(pk=fecha_pk)
	partidos = Partido.objects.filter(fecha=fecha)
	_pronosticos = Pronostico.objects.filter(participante=participante,partido__in=partidos)

	_pron = {}
	for pa in partidos:
		for pr in _pronosticos:
			if pa == pr.partido:
				_pron[pa] = pr
				break
		if not pa in _pron.keys():
			_pron[pa] = None

	partido_pronostico = _pron
	context = {
		"prode": prode,
		"participante": participante,
		"partidos": partidos,
		"pronosticos": _pronosticos,
		"pp": partido_pronostico,
		"p_pk": pronostico_pk,
	}


	form = EditarPronosticoForm()
	

	if request.method == "POST":
		form = EditarPronosticoForm(request.POST)
		if form.is_valid():
			_pronostico = Pronostico.objects.get(pk=pronostico_pk)
			_pronostico.resultado = form.cleaned_data["resultado"]

			_pronostico.save()

			#return redirect(request, "pronosticos.html", context)
			return redirect("/{}/participantes/{}/pronosticos/{}/".format(prode_pk,participante_pk,fecha_pk))

	context = {
		"prode": prode,
		"participante": participante,
		"partidos": partidos,
		"pronosticos": _pronosticos,
		"pp": partido_pronostico,
		"p_pk": pronostico_pk,
		"form": form,
	}
	
	return render(request, "editar_pronosticos.html", context)

def nuevo_pronostico(request, prode_pk, participante_pk, fecha_pk, partido_pk):
	prode = Prode.objects.get(pk=prode_pk)
	participante = Participante.objects.get(pk=participante_pk)
	fecha = Fecha.objects.get(pk=fecha_pk)
	partidos = Partido.objects.filter(fecha=fecha)
	_pronosticos = Pronostico.objects.filter(participante=participante,partido__in=partidos)

	_pron = {}
	for pa in partidos:
		for pr in _pronosticos:
			if pa == pr.partido:
				_pron[pa] = pr
				break
		if not pa in _pron.keys():
			_pron[pa] = None


	for k,v in _pron.items():
		if(v):
			print("{} - {} apues: {} real: {}"
			.format(k.local, k.visitante, v.resultado, k.resultado))
		else:
			print("{} - {} apues: {} real: {}"
			.format(k.local, k.visitante, "-", k.resultado))
	partido_pronostico = _pron
	#partido_pronostico = dict(zip(partidos, _pron))
	
	


	form = EditarPronosticoForm()
	
	if request.method == "POST":
		form = EditarPronosticoForm(request.POST)
		if form.is_valid():
			partido = Partido.objects.get(pk=partido_pk)
			
			print(partido.pk)
			print("------------------")
			print(partido.local, partido.visitante)
			_pronostico = Pronostico(
				resultado=form.cleaned_data["resultado"],
				participante=participante,
				partido=partido
			)

			_pronostico.save()

			#return pronosticos(request, prode_pk, participante_pk, fecha_pk)
			context = {
				"prode": prode,
				"participante": participante,
				"partidos": partidos,
				"pronosticos": _pronosticos,
				"pp": partido_pronostico,
				"p_pk": partido_pk,
			}
			return redirect("/{}/participantes/{}/pronosticos/{}/".format(prode_pk,participante_pk,fecha_pk))
			
	context = {
		"prode": prode,
		"participante": participante,
		"partidos": partidos,
		"pronosticos": _pronosticos,
		"pp": partido_pronostico,
		"p_pk": partido_pk,
		"form": form,
		"nuevo": True,
	}	
	return render(request, "editar_pronosticos.html", context)

def editar_partido(request, prode_pk, fecha_pk, partido_pk):
	form = EditarPronosticoForm()
	prode = Prode.objects.get(pk=prode_pk)
	fecha = Fecha.objects.get(pk=fecha_pk)
	partidos = Partido.objects.filter(fecha=fecha)

	if request.method == "POST":	
		form = EditarPronosticoForm(request.POST)
		if form.is_valid():
			part = Partido.objects.get(pk=partido_pk) 

			part.resultado=form.cleaned_data["resultado"]
			
			part.save()

			return fecha_partidos(request, prode_pk, fecha_pk)	

	context = {
		"prode": prode,
		"fecha": fecha,
		"form": form,
		"partidos": partidos,
		"partido_pk": partido_pk
	}				
	return render(request, "editar_partido.html", context)

def tabla_fecha(request, prode_pk, fecha_pk):
	prode = Prode.objects.get(pk=prode_pk)
	fecha = Fecha.objects.get(pk=fecha_pk)
	partidos = Partido.objects.filter(fecha=fecha)
	participantes = Participante.objects.filter(prode=prode)
	
	pronosticos_participantes = {x: Pronostico.objects.filter(participante=x,partido__in=partidos) for x in participantes}
	
	for k,v in pronosticos_participantes.items():
		f = []
		aux = False
		for part in partidos:
			for p in v:
				if p.partido == part:
					f.append(p)
					aux = True
			if not aux:
				f.append(None)
			aux = False


		pronosticos_participantes[k] = f
	
	print(pronosticos_participantes)
	context = {
		"prode": prode,
		"fecha": fecha,
		"partidos": partidos,
		"pronosticos_participantes": pronosticos_participantes,
	}
	return render(request, "tabla_fecha.html", context)	

def tabla_puntos(request, prode_pk):
	prode = Prode.objects.get(pk=prode_pk)
	participantes = prode.participantes.all()
	fechas = Fecha.objects.filter(prode=prode)
	partidos = Partido.objects.filter(fecha__in=fechas)
	#participantes = Participante.objects.filter(prode=prode)
	
	#participante_ptos = {}
	participante_ptos = []

	check_s = lambda x,y,op: op(x.split("-")[0],  x.split("-")[1]) and op(y.split("-")[0], y.split("-")[1]) and x != y
	for participante in participantes:
		pronosticos = Pronostico.objects.filter(participante=participante,partido__in=partidos)
		ptos = 0
		plenos = 0
		for partido in partidos:
			for pronostico in pronosticos:

				if partido == pronostico.partido and partido.resultado != "-" and pronostico.resultado != "-" and partido.resultado != "" and pronostico.resultado != "": 
					pro = pronostico.resultado
					par = partido.resultado
					
					if par == pro:
						ptos += 3
						plenos += 1
					elif check_s(par, pro, operator.lt) or check_s(par, pro, operator.gt) or check_s(par, pro, operator.eq):
						ptos += 1

		participante_ptos.append([participante.nombre, ptos, plenos]) 

	
	participante_ptos.sort(key = lambda arr: (arr[1], arr[2]), reverse=True)
	context = {
		"prode": prode,
		"participante_ptos": participante_ptos,
	}
	return render(request, "tabla_puntos.html", context)
