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
from core.views import tela_login, tela_estoque
from core.views import criar_categoria, editar_categoria, excluir_categoria
from core.views import criar_mercadoria, editar_mercadoria, excluir_mercadoria, listar_mercadorias
from core.views import criar_pessoa, editar_pessoa, excluir_pessoa, listar_pessoas
from core.views import ListarCategoriasView, NovaCategoriaView, ExcluirCategoriaView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home),


    path('tela_login/', tela_login),
    path('tela_estoque/', tela_estoque),


    # path('listar_categoria/', listar_categoria),
    # path('criar_categoria/', criar_categoria),
    path('editar_categoria/', editar_categoria),
    path('excluir_categoria/', excluir_categoria),


    path('listar_categoria', ListarCategoriasView.as_view(), name='listar_categorias'),
    path('criar_categoria', NovaCategoriaView.as_view(), name='criar_categoria'),
    # path('excluir_categoria/<int:pk>', ExcluirCategoriaView.as_view(), name='excluir-categoria'),


    path('criar_mercadoria/', criar_mercadoria),
    path('listar_mercadorias/', listar_mercadorias),
    path('editar_mercadoria/', editar_mercadoria),
    path('excluir_mercadoria/', excluir_mercadoria),


    path('criar_pessoa/', criar_pessoa),
    path('listar_pessoas/', listar_pessoas),
    path('editar_pessoa/', editar_pessoa),
    path('excluir_pessoa/', excluir_pessoa),
]
