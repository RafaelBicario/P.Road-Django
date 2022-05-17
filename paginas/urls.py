from django.urls import path
from .views import Index

from .views import CidadeCreate, PessoaCreate
from .views import CidadeUpdate, PessoaUpdate
from .views import CidadeDelete, PessoaDelete
from .views import CidadeList

urlpatterns = [
    path('', Index.as_view(), name='index'),

    path('cadastrar/cidade/', CidadeCreate.as_view(), name='cadastrar-cidade'),
    path('cadastrar/pessoa/', PessoaCreate.as_view(), name='cadastrar-pessoa'),


    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name='editar-cidade'),
    path('editar/pessoa/<int:pk>/', PessoaUpdate.as_view(), name='editar-pessoa'),


    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name='deletar-cidade'),
    path('excluir/pessoa/<int:pk>/', PessoaDelete.as_view(), name='deletar-pessoa'),


    path('listar/cidade', CidadeList.as_view(), name='listar-cidade'),

]