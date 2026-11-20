from django.shortcuts import render
from .models import Tarefa

def inicio(request):
    return render(request, "tarefas/inicio.html")

def lista_tarefas(request):
    tarefas = Tarefa.objects.all().order_by("data_prevista")

    return render(request, "tarefas/lista.html", {"tarefas": tarefas})
def home(request):
    return render(request, "tarefas/home.html")