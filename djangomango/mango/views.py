"""
Por aqui criamos o que será visto pelo usuário, seja a parte lógica ou a visual, por aqui
levaremos o usuário para diferentes páginas html de acordo com testes lógicos
"""
import json
from django.shortcuts import render, redirect
from django.db.models import F
from .models import AlimentoClicavel

def index(request):
    manga = AlimentoClicavel.objects.get(id=1)
    #cliques_manga = request.session.get('cliques_manga', 0)
    context = {'cliques_manga': manga.cliques}
    return render(request, 'mango/index.html', context)

def clicked(request):
    AlimentoClicavel.objects.filter(id=1).update(cliques=F('cliques') + 1)
    #request.session['cliques_manga'] = request.session.get('cliques_manga', 0) + 1
    return redirect('index')