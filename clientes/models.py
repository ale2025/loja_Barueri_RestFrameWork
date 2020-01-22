from django.db import models


class Cadastro(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255)
    email = models.EmailField()
    data_de_nascimento = models.CharField(max_length=255)
    idade = models.IntegerField()