from django.db import models

class aluno(models.Model):
    id = models.IntegerField(default=11, primary_key=True)
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10, blank=True, null=True) #blank=True, null=True campo pode ser vazio
    email = models.CharField(max_length=50)

class tipo_ingresso(models.Model):
    id = models.IntegerField(default=11, primary_key=True)
    tipoIngresso = models.CharField(max_length=50)

class departamento(models.Model):
    id = models.IntegerField(default=11, primary_key=True)
    nome = models.CharField(max_length=20)
    bloco = models.CharField(max_length=1)