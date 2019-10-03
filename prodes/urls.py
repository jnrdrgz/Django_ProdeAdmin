from django.urls import path
from prodes import views

urlpatterns = [
	path('', views.prodes, name="prodes"),
	path("agregar_prode/", views.agregar_prode, name="agregar_prode"),
	path("<int:pk>/", views.prode_menu, name="prode_menu"),
	path("<int:pk>/participantes/", views.participantes_menu, name="participantes_menu"),
	path("<int:prode_pk>/participantes/<int:participante_pk>/", views.participante, name="participante"),
	path("<int:prode_pk>/participantes/<int:participante_pk>/pronosticos", views.pronosticos_menu, name="pronosticos_menu"),
	path("<int:prode_pk>/participantes/<int:participante_pk>/<int:fecha_pk>", views.pronosticos, name="pronosticos"),
	path("<int:pk>/agregar_participante/", views.agregar_participante, name="agregar_participante"),
	path("<int:pk>/fechas/", views.fechas_menu, name="fechas_menu"),
	path("<int:pk>/agregar_fecha/", views.agregar_fecha, name="agregar_fecha"),
	path("<int:prode_pk>/fechas/<int:fecha_pk>/", views.fecha, name="fecha"),
	path("<int:prode_pk>/fechas/<int:fecha_pk>/partidos/", views.fecha_partidos, name="fecha_partidos"),
	path("<int:prode_pk>/fechas/<int:fecha_pk>/agregar_partido/", views.agregar_partido, name="agregar_partido"),
]


