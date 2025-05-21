from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin
# Create your models here

class AlimentoClicavel(models.Model):
    nome = models.CharField()
    cliques = models.IntegerField()
    dia_mais_clicado = models.DateField()
    def __str__(self):
        return self.nome
    """
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    """