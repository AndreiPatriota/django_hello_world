from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone

class TodosCursos(models.Model):
    nomecursos = models.CharField(max_length=200)
    nomeinstruct = models.CharField(max_length=100)
    inicio = models.DateTimeField('Started from')

    def __str__(self):
        return self.nomecursos

    def faz_tempo(self):
         return self.inicio >= timezone.now() - timedelta(days=1)


class Detalhes(models.Model):
    curso = models.ForeignKey(TodosCursos, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    opção = models.BooleanField(default=False)

    def __str__(self):
        return str(self.tipo)