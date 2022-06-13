# from inspect import _void
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

# ======================================================================================================================
#
# class Motoristas(models.Model):
#     nome_completo = models.CharField(max_lenght=50, verbose_name='Informe o Nome')
#     nascimento = models.DateField(verbose_name='Informe a Data de Nascimento')
#     telefone = models.CharField(max_length=20, verbose_name='Informe o Telefone')
#     email = models.EmailField(max_length=100, unique=True)
#     rg = models.CharField(max_length=20, verbose_name="Informe o RG")
#     cpf = models.CharField(max_length=20, verbose_name="Informe o CPF")
#
# class Veiculo(models.Model):
#     placa = models.CharField(max_length=50)
#     modelo = models.CharField(max_length=50)
#
# class Viagens(models.Model):
#     local = models.CharField(max_length=50)
#
#
# class Clientes(models.Model):
#     nome_completo = models.CharField(max_length=50, verbose_name="Informe o Nome",
#     help_text="Digite seu nome completo")
#     telefone = models.CharField(max_length=20, verbose_name='Informe o Telefone')
#     nascimento = models.DateField(verbose_name='Informe a Data de Nacimento')
#     email = models.EmailField(max_length=100, unique=True)
#     rg = models.CharField(max_length=20, verbose_name="Informe o RG")
#     cpf = models.CharField(max_length=20, verbose_name="Informe o CPF")
#
#     def __str__(self) -> str:
#         return '{} ({})'.format(self.nome_completo, self.nascimento, self.email, self.rg, self.cpf)

# ======================================================================================================================
