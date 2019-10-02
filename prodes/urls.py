from django.urls import path
from prodes import views

urlpatterns = [
	path('', views.prodes, name="prodes"),
	path("agregar_prode/", views.agregar_prode, name="agregar_prode"),
	path("<int:pk>/", views.prode_menu, name="prode_menu"),
	path("<int:pk>/participantes/", views.participantes_menu, name="participantes_menu"),
	path("<int:pk>/agregar_participante/", views.agregar_participante, name="agregar_participante"),
	path("<int:pk>/fechas/", views.fechas_menu, name="fechas_menu"),
	path("<int:prode_pk>/fechas/<int:fecha_pk>", views.fecha, name="fecha"),
	path("<int:prode_pk>/fechas/<int:fecha_pk>/partidos/", views.fecha_partidos, name="fecha_partidos"),
]


