from audioop import reverse
from pyexpat import model
from re import template

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
# from braces.views import GroupRequiredMixin
#
# =====================================================
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView , DeleteView
from .models import Cidade, Pessoa, Veiculo, Clientes, Viagens, Motoristas  # importar as classes do model.py
from django.views.generic.list import ListView
# =====================================================

# Create your views here.
class Index(TemplateView):
    template_name = 'paginas/index.html'


#CreateView=============================================================================================================
class CidadeCreate(CreateView): # padrão de nome : Nome_da_classe + Create
    model = Cidade
    fields = ['nome','estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')

class PessoaCreate(CreateView):
    model = Pessoa
    fields = ['nome_completo','nascimento','email','cidade']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')

class VeiculoCreate(CreateView):
    model = Veiculo
    fields = ['placa','modelo']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')

class ClientesCreate(CreateView):
    model = Clientes
    fields = ['nome_completo','telefone','nascimento','email','rg','cpf']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class ViagensCreate(CreateView):
    model = Viagens
    fields = ['local_saida','local_destino','parada','usuario']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')

class MotoristaCreate(CreateView):
    model = Motoristas
    fields = ['nome_completo','telefone','nascimento','email','rg','cpf']
    template_name = 'paginas/form.html'
    group_required = u"Motoristas"
    success_url = reverse_lazy('index')

#UpdateView=============================================================================================================
class CidadeUpdate(UpdateView):
    model = Cidade
    fields = ['nome','estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')

class PessoaUpdate(UpdateView):
    model = Pessoa
    fields = ['nome_completo','nascimento','email','cidade']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')

class VeiculoUpdate(UpdateView):
    model = Veiculo
    fields = ['placa','modelo']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')

class ClientesUpdate(UpdateView):
    model = Clientes
    fields = ['nome_completo','telefone','nascimento','email','rg','cpf']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')

class ViagensUpdate(UpdateView):
    model = Viagens
    fields = ['local_saida', 'local_destino', 'parada']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')

class MotoristaUpdate(UpdateView):
    model = Motoristas
    fields = ['nome_completo','telefone','nascimento','email','rg','cpf']
    template_name = 'paginas/form.html'
    group_required = u"Motoristas"
    success_url = reverse_lazy('index')

#DeleteView=============================================================================================================
class CidadeDelete(DeleteView):
    model = Cidade
    group_required = [u"admin", u"Motoristas"]
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-cidade')

class PessoaDelete(DeleteView):
    model = Pessoa
    group_required = [u"admin", u"Motoristas"]
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('index')

class VeiculoDelete(DeleteView):
    model = Veiculo
    group_required = [u"admin", u"Motoristas"]
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('index')

class ClientesDelete(DeleteView):
    model = Clientes
    group_required = [u"admin", u"Motoristas"]
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('index')

class ViagensDelete(DeleteView):
    model = Viagens
    group_required = [u"admin", u"Motoristas"]
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('index')

class MotoristaDelete(DeleteView):
    model = Motoristas
    group_required = u"Motoristas"
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('index')


#ListView===============================================================================================================
class CidadeList(ListView):
    model = Cidade
    template_name = 'paginas/listas/cidades.html'

class ClienteList(ListView):
    model = Clientes
    context_object_name = 'cliente'
    template_name = 'paginas/listas/clientes.html'

class VeiculoList(ListView):
    model = Veiculo
    template_name = 'paginas/listas/veiculos.html'

class ViagensList(ListView):
    model = Viagens
    template_name = 'paginas/listas/viagens.html'

class MotoristaList(ListView):
    model = Motoristas
    template_name = 'paginas/listas/motoristas.html'


# class CidadeList(GroupRequiredMixin, LoginRequiredMixin, ListView):
#     login_url = reverse_lazy('login')
#     group_required = u"Administrador"
#     model = Cidade
#     template_name = 'cadastros/listar_estados.html'
