from django.urls import path
from .views import Index

from .views import MotoristaCreate, VeiculoCreate, ViagensCreate, ClientesCreate, CidadeCreate, PessoaCreate
from .views import MotoristaUpdate, VeiculoUpdate, ViagensUpdate,ClientesUpdate, CidadeUpdate, PessoaUpdate
from .views import MotoristaDelete, VeiculoDelete, ViagensDelete, ClientesDelete, CidadeDelete, PessoaDelete
from .views import ClienteList, MotoristaList, VeiculoList, ViagensList, CidadeList

urlpatterns = [
    path('', Index.as_view(), name='index'),

    path('cadastrar/cidade/', CidadeCreate.as_view(), name='cadastrar-cidade'),
    path('cadastrar/pessoa/', PessoaCreate.as_view(), name='cadastrar-pessoa'),
    path('cadastrar/cliente/', ClientesCreate.as_view(), name='cadastrar-clientes'),
    path('cadastrar/veiculo/', VeiculoCreate.as_view(), name='cadastrar-veiculo'),
    path('cadastrar/viagens/', ViagensCreate.as_view(), name='cadastrar-viagens'),
    path('cadastrar/motorista/', MotoristaCreate.as_view(), name='cadastrar-viagens'),


    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name='editar-cidade'),
    path('editar/pessoa/<int:pk>/', PessoaUpdate.as_view(), name='editar-pessoa'),
    path('editar/cliente/<int:pk>/', ClientesUpdate.as_view(), name='editar-clientes'),
    path('editar/veiculo/<int:pk>/', VeiculoUpdate.as_view(), name='editar-veiculos'),
    path('editar/viagens/<int:pk>/', ViagensUpdate.as_view(), name='editar-viagens'),
    path('editar/motorista/<int:pk>/', MotoristaUpdate.as_view(), name='editar-motorista'),


    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name='deletar-cidade'),
    path('excluir/pessoa/<int:pk>/', PessoaDelete.as_view(), name='deletar-pessoa'),
    path('excluir/cliente/<int:pk>/', ClientesDelete.as_view(), name='deletar-clientes'),
    path('excluir/veiculo/<int:pk>/', VeiculoDelete.as_view(), name='deletar-veiculo'),
    path('excluir/viagens/<int:pk>/', ViagensDelete.as_view(), name='deletar-viagens'),
    path('excluir/motorista/<int:pk>/', MotoristaDelete.as_view(), name='deletar-motorista'),


    path('listar/cidade', CidadeList.as_view(), name='listar-cidade'),
    path('listar/cliente', ClienteList.as_view(), name='listar-cliente'),
    path('listar/motorista', MotoristaList.as_view(), name='listar-motorita'),
    path('listar/veiculo', VeiculoList.as_view(), name='listar-veiculo'),
    path('listar/viagens', ViagensList.as_view(), name='listar-viagens'),
    path('listar/motorista', MotoristaList.as_view(), name='listar-motorita'),

]