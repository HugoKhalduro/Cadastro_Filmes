from django.db import models
from django.utils import timezone

class Filme(models.Model):
    diretor = models.CharField(max_length=200)
    nome_filme = models.CharField(max_length=200)
    elenco = models.CharField(max_length=200)
    produtora = models.CharField(max_length=200)
    roterista = models.CharField(max_length=200)



    def __str__(self):
        return self.nome_filme
