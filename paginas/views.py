from audioop import reverse
from pyexpat import model
from re import template
from django.views.generic import TemplateView

# =====================================================
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView , DeleteView
from .models import Cidade, Pessoa # importar as classes do model.py
from django.views.generic.list import ListView
# =====================================================

# Create your views here.
class Index(TemplateView):
    template_name = 'paginas/index.html'


#CreateView
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


#UpdateView
class CidadeUpdate(UpdateView): # padrão de nome : Nome_da_classe + Update
    model = Cidade
    fields = ['nome','estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')

class PessoaUpdate(UpdateView):
    model = Pessoa
    fields = ['nome_completo','nascimento','email','cidade']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


#DeleteView
class CidadeDelete(DeleteView):
    model = Cidade
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-cidade')

class PessoaDelete(DeleteView):
    model = Pessoa
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('index')



class CidadeList(ListView):
    model = Cidade
    template_name = 'paginas/listas/cidades.html'