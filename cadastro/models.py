from django.db import models


class Caminhao(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    placa = models.CharField(max_length=10)
    ano = models.IntegerField()
    hora_cadastro = models.DateTimeField(auto_now_add=True)