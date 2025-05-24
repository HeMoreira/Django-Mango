from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin
# Create your models here

class AlimentoClicavel(models.Model):
    nome = models.CharField()
    cliques = models.IntegerField(default=0)
    cliques_de_hoje = models.IntegerField(default=0)
    cliques_do_dia_mais_clicado = models.IntegerField(default=0)
    dia_mais_clicado = models.DateField(default=timezone.now())
    def __str__(self):
        return self.nome

class DiaAtual(models.Model):
    dia_ultima_requisicao = models.DateField(default=timezone.now())
    """
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    """