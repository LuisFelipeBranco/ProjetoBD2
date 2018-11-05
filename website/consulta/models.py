from django.db import models

class aluno(models.Model):
    id = models.IntegerField(default=11, primary_key=True)
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10, blank=True, null=True) #blank=True, null=True campo pode ser vazio
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class tipo_ingresso(models.Model):
    id = models.IntegerField(default=11, primary_key=True)
    tipoIngresso = models.CharField(max_length=50)

class departamento(models.Model):
    id = models.IntegerField(default=11, primary_key=True)
    nome = models.CharField(max_length=20)
    bloco = models.CharField(max_length=1)

    def __str__(self):
        return self.nome

class situacao_matricula(models.Model):
    id = models.IntegerField(default=11, primary_key=True)
    descricao = models.CharField(max_length=15)

class curso(models.Model):
    id = models.IntegerField(default=11, primary_key=True)
    id_dpto = models.ForeignKey(departamento, on_delete=models.CASCADE)
    nome = models.CharField(max_length=20)
    descricao = models.CharField(max_length=15)

    def __str__(self):
        return self.nome