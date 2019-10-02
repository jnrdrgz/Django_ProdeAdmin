from django.urls import path
from prodes import views

urlpatterns = [
	path('', views.prodes, name="prodes"),
	path("agregar_prode/", views.agregar_prode, name="agregar_prode"),
	path("<int:pk>/", views.prode_menu, name="prode_menu"),
	path("<int:pk>/participantes", views.participantes_menu, name="participantes_menu"),
	path("<int:pk>/fechas", views.fechas_menu, name="fechas_menu"),
]


