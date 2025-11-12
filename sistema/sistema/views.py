from django.shortcuts import render
from .models import Tarefa

def index(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'sistema/index.html', {'tarefas': tarefas})

def problema(request):
    return render(request, 'sistema/problema.html')

def solucao(request):
    return render(request, 'sistema/solucao.html')

def autor(request):
    return render(request, 'sistema/autor.html')
