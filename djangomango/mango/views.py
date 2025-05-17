"""
Por aqui criamos o que será visto pelo usuário, seja a parte lógica ou a visual, por aqui
levaremos o usuário para diferentes páginas html de acordo com testes lógicos
"""

from django.shortcuts import render

def index(request):
    return render(request, 'mango/index.html')