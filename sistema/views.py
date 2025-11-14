from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from django.views.decorators.http import require_POST
def index(request):
    tarefas = Tarefa.objects.all().order_by('-criado_em')
    return render(request, 'sistema/index.html', {'tarefas': tarefas})
def problema(request):
    return render(request, 'sistema/problema.html')
def solucao(request):
    return render(request, 'sistema/solucao.html')
def autor(request):
    return render(request, 'sistema/autor.html')
@require_POST
def adicionar_tarefa(request):
    titulo = request.POST.get('titulo','').strip()
    descricao = request.POST.get('descricao','').strip()
    if titulo:
        Tarefa.objects.create(titulo=titulo, descricao=descricao)
    return redirect('index')
def toggle_concluir(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    tarefa.concluida = not tarefa.concluida
    tarefa.save()
    return redirect('index')
def remover(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    tarefa.delete()
    return redirect('index')
