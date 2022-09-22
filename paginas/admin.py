from django.contrib import admin
from .models import Motoristas, Cidade, Pessoa, Clientes, Veiculo, Viagens

# Register your models here.
admin.site.register(Cidade)
admin.site.register(Pessoa)
admin.site.register(Clientes)
admin.site.register(Viagens)
admin.site.register(Veiculo)
admin.site.register(Motoristas)

