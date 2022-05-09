from django.urls import path
from .views import Index

from .views import CidadeCreate, PessoaCreate
from .views import CidadeUpdate, PessoaUpdate

urlpatterns = [
    path('', Index.as_view(), name='index'),

    path ('cadastrar/cidade/', CidadeCreate.as_view(),nome='cadastrar-cidade'),
    path ('cadastrar/pessoa/', PessoaCreate.as_view(),nome='cadastrar-pessoa'),

    path ('editar/cidade/<int:pk>/', CidadeUpdate.as_view(),nome='editar-cidade'),
    path ('editar/pessoa/<int:pk>/', PessoaUpdate.as_view(),nome='editar-pessoa'),

]