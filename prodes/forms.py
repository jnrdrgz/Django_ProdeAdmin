from django import forms

class NuevoProdeForm(forms.Form):
	nombre = forms.CharField(
		max_length=120,
		widget=forms.TextInput(attrs={
			"class": "form-control",
			"placeholder": "Nombre"
		})
	)

class NuevaFechaForm(forms.Form):
	numero = forms.IntegerField(
		widget=forms.TextInput(attrs={
			"class": "form-control"
		})
	)

class NuevoParticipanteForm(forms.Form):
	nombre = forms.CharField(
		max_length=120,
		widget=forms.TextInput(attrs={
			"class": "form-control",
			"placeholder": "Nombre"
		})
	)

class NuevoPartidoForm(forms.Form):
	local = forms.CharField(
		max_length=120,
		widget=forms.TextInput(attrs={
			"class": "form-control",
			"placeholder": "Local"
		})
	)

	visitante = forms.CharField(
		max_length=120,
		widget=forms.TextInput(attrs={
			"class": "form-control",
			"placeholder": "Visitante"
		})
	)

	resultado = forms.CharField(
		max_length=10,
		widget=forms.TextInput(attrs={
			"class": "form-control",
			"placeholder": ""
		}),
		required=False
	)

class EditarPronosticoForm(forms.Form):
	resultado = forms.CharField(
		max_length=10,
		widget=forms.TextInput(attrs={
			"class": "form-control",
			"placeholder": ""
		}),
		required=False
	)