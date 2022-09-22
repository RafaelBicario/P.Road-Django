# from inspect import _void
from django.db import models
from django.contrib.auth.models import User

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

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return '{} ({})'.format(self.nome_completo, self.nascimento, self.email, self.cidade)


# ======================================================================================================================



# ======================================================================================================================
#
class Motoristas(models.Model):
    nome_completo = models.CharField(max_length=50, verbose_name="Informe o Nome",
                                     help_text="Digite seu nome completo")
    telefone = models.CharField(max_length=20, verbose_name='Informe o Telefone')
    nascimento = models.DateField(verbose_name='Informe a Data de Nacimento')
    email = models.EmailField(max_length=100, unique=True)
    rg = models.CharField(max_length=20, verbose_name="Informe o RG")
    cpf = models.CharField(max_length=20, verbose_name="Informe o CPF")

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return '{} ({})'.format(self.nome_completo, self.nascimento, self.email, self.rg, self.cpf)

#
class Veiculo(models.Model):
    placa = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return '{} ({})'.format(self.placa, self.modelo)

#
class Viagens(models.Model):
    local_saida = models.CharField(max_length=50)
    local_destino = models.CharField(max_length=50)
    parada = models.CharField(max_length=50)

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return '{} ({})'.format(self.local_destino, self.local_saida, self.parada)
#
class Clientes(models.Model):
    nome_completo = models.CharField(max_length=50, verbose_name="Informe o Nome",
    help_text="Digite seu nome completo")
    telefone = models.CharField(max_length=20, verbose_name='Informe o Telefone')
    nascimento = models.DateField(verbose_name='Informe a Data de Nacimento')
    email = models.EmailField(max_length=100, unique=True)
    rg = models.CharField(max_length=20, verbose_name="Informe o RG")
    cpf = models.CharField(max_length=20, verbose_name="Informe o CPF")

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return '{} ({})'.format(self.nome_completo, self.nascimento, self.email, self.rg, self.cpf)

# ======================================================================================================================



# def from_valid (Self,form):

# form.instance.usuario = self.request.user

#   url = super().form_valid(form)
#   return url