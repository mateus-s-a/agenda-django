from django.urls import path

from agenda.views import listar_evento, exibir_evento, participar_evento

urlpatterns = [ # --- são as rotas para as views
    path("eventos/", listar_evento, name="listar_eventos"),
    path("eventos/<int:id>/", exibir_evento, name="exibir_evento"),
    path("participar/", participar_evento, name="participar_evento"),
]