"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from turtle import home

from django.contrib import admin
from django.urls import path

from core.views import home
from core.views import tela_estoque
from core.views import ListarCategoriaView, NovaCategoriaView, EditarCategoriaView, ExcluirCategoriaView
from core.views import ListarEstoqueView, NovoEstoqueView, EditarEstoqueView, ExcluirEstoqueView
from core.views import CriarPessoasView, ListarPessoasView,EditarPessoaView, ExcluirPessoaView
from core.views import TelaLoginView
from core.views import ListarMovimentacaoView, CriarMovimentacaoView, FinalizarMovimentacaoView
from core.views import DespacharView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),


    path('login/', TelaLoginView.as_view(), name='login'),
    path('tela_estoque/', tela_estoque, name='estoque'),


    # Paths usando CBV (class based view)
    path('listar_categoria/', ListarCategoriaView.as_view(), name='listar_categoria'),
    path('criar_categoria/', NovaCategoriaView.as_view(), name='criar_categoria'),
    path('editar_categoria/<int:pk>', EditarCategoriaView.as_view(), name='editar_categoria'),
    path('excluir_categoria/<int:pk>', ExcluirCategoriaView.as_view(), name='excluir_categoria'),


    path('listar_mercadoria/', ListarEstoqueView.as_view(), name='listar_mercadoria'),
    path('criar_mercadoria/', NovoEstoqueView.as_view(), name='criar_mercadoria'),
    path('editar_mercadoria/<int:pk>', EditarEstoqueView.as_view(), name='editar_mercadoria'),
    path('excluir_mercadoria/<int:pk>', ExcluirEstoqueView.as_view(), name='excluir_mercadoria'),


    path('listar_pessoa/', ListarPessoasView.as_view(), name='listar_pessoa'),
    path('criar_pessoa/', CriarPessoasView.as_view(), name='criar_pessoa'),
    path('editar_pessoa/<int:pk>/', EditarPessoaView.as_view(), name='editar_pessoa'),
    path('excluir_pessoa/<int:pk>', ExcluirPessoaView.as_view(), name='excluir_pessoa'),


    path('listar_mercadoria_despachada/', ListarMovimentacaoView.as_view(), name='listar_mercadoria_despachada'),
    # path('criar_movimentacao/<int:pk>/', CriarMovimentacaoView.as_view(), name='criar_movimentacao'),
    path('finalizar_mercadoria_despachada/<int:pk>/', FinalizarMovimentacaoView.as_view(), name='finalizar_mercadoria_despachada'),

    path('despachar/<int:pk>/', DespacharView.as_view(), name='despachar'),
]
