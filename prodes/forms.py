from django import forms

class NuevoProdeForm(forms.Form):
	nombre = forms.CharField(
		max_length=120,
		widget=forms.TextInput(attrs={
			"class": "form-control",
			"placeholder": "Nombre"
		})
	)