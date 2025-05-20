"""
Esse arquivo é responsavel por mapear as urls possíveis do seu site, necessário para
que o servidor seja capaz de encontrar os determinados caminhos quando forem acessados
por um usuário.
Após adicionar a url por aqui, também precisamos registra-la em urls.py de mysite
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("clicked", views.clicked, name="clicked"),
]