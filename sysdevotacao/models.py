from django.db import models
from django.utils import timezone

class escola(models.Model):
    name = models.CharField(max_length=180)
    def __str__(self):
        return self.name

class turmas(models.Model):
    data_incricao = models.DateTimeField( default=timezone.now,editable=False)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(max_length=600)
    nomeAplicativo = models.CharField(max_length=180)
    linkYoutube = models.CharField(max_length=180)
    nomeEquipe =  models.CharField(max_length=180)
    votos = models.PositiveBigIntegerField(default=0)


    def __str__(self):
        return self.titulo