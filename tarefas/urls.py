from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("inicio/", views.inicio, name="inicio"),
    path("tarefas/", views.lista_tarefas, name="lista_tarefas"),
]