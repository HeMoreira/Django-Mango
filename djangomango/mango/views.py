"""
Por aqui criamos o que será visto pelo usuário, seja a parte lógica ou a visual, por aqui
levaremos o usuário para diferentes páginas html de acordo com testes lógicos
"""
import json
from django.utils import timezone
from django.shortcuts import render, redirect
from django.db.models import F
from .models import AlimentoClicavel
from .models import DiaAtual

def index(request):
    manga = AlimentoClicavel.objects.get(id=1)
    context = {'cliques_manga': manga.cliques, 'dia_mais_clicado_manga': manga.dia_mais_clicado, 'cliques_do_dia_mais_clicado_manga': manga.cliques_do_dia_mais_clicado, 'cliques_de_hoje_manga': manga.cliques_de_hoje}
    data_atual = timezone.now()
    hoje = data_atual.strftime('%Y-%m-%d')
    if DiaAtual.objects.get(id=1).dia_ultima_requisicao.strftime('%Y-%m-%d') != hoje:
        DiaAtual.objects.filter(id=1).update(dia_ultima_requisicao=timezone.now())
        AlimentoClicavel.objects.filter(id=1).update(cliques_de_hoje=0)
        print("aaaaaaaaaaaaaaaa")
        return render(request, 'mango/index.html', context)
    else:
        return render(request, 'mango/index.html', context)

def clicked(request):
    AlimentoClicavel.objects.filter(id=1).update(cliques=F('cliques') + 1)
    AlimentoClicavel.objects.filter(id=1).update(cliques_de_hoje=F('cliques_de_hoje') + 1)
    if AlimentoClicavel.objects.get(id=1).cliques_de_hoje == AlimentoClicavel.objects.get(id=1).cliques_do_dia_mais_clicado:
        AlimentoClicavel.objects.filter(id=1).update(dia_mais_clicado=timezone.now())
        AlimentoClicavel.objects.filter(id=1).update(cliques_do_dia_mais_clicado=AlimentoClicavel.objects.get(id=1).cliques_de_hoje)
    if AlimentoClicavel.objects.get(id=1).cliques_de_hoje > AlimentoClicavel.objects.get(id=1).cliques_do_dia_mais_clicado:
        AlimentoClicavel.objects.filter(id=1).update(cliques_do_dia_mais_clicado=F('cliques_do_dia_mais_clicado') + 1)
    return redirect('index')

