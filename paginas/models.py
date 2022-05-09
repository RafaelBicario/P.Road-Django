from inspect import _void
from django.db import models

ESTADOS = {
    ('PR', 'Paraná'),
    ('SP', 'São Paulo'),
    ('RJ', 'Rio de Janeiro'),
    ('SC', 'Santa Catarina'),
}

class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.CharField(max_length=2, choices=ESTADOS)

class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=50, verbose_name=" Qual seu nome?", help_text="Digite seu nome completo")
    nascimento = models.DateField(verbose_name='data de nascimento')
    email = models.EmailField(max_length=100, unique=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return '{} ({})'.format(self.nome_completo, self.nascimento)
