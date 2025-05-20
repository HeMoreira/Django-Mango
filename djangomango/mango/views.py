"""
Por aqui criamos o que será visto pelo usuário, seja a parte lógica ou a visual, por aqui
levaremos o usuário para diferentes páginas html de acordo com testes lógicos
"""
import json
from django.shortcuts import render, redirect

context = {
    'cliques_manga': 0
}

def index(request):
    cliques_manga = request.session.get('cliques_manga', 0)
    context = {'cliques_manga': cliques_manga}
    return render(request, 'mango/index.html', context)

def clicked(request):
    request.session['cliques_manga'] = request.session.get('cliques_manga', 0) + 1
    return redirect('index')