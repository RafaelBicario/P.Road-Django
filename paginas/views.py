from audioop import reverse
from pyexpat import model
from re import template
from django.views.generic import TemplateView

# =====================================================
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .models import Cidade, Pessoa # importar as classes do model.py
# =====================================================

# Create your views here.
class Index(TemplateView):
    template_name = 'paginas/index.html'



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



class CidadeUpdate(UpdateView): # padrão de nome : Nome_da_classe + Create
    model = Cidade
    fields = ['nome','estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')

class PessoaUpdate(UpdateView):
    model = Pessoa
    fields = ['nome_completo','nascimento','email','cidade']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')