from django.shortcuts import redirect, render, get_object_or_404

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.views.generic import CreateView, ListView, DeleteView, View
from django.urls import reverse_lazy

from core.models import Categoria

# Create your views here.
def home(request):
    return render(request, "core/home.html" ) 



# def listar_categoria(request):
#     return render(request, "core/listar_categoria.html" ) 

def criar_categoria(request):
    return render(request, "core/criar_categoria.html" )

def editar_categoria(request):
    return render(request, "core/editar_categoria.html" ) 

def excluir_categoria(request):
    return render(request, "core/excluir_categoria.html" )




class ListarCategoriasView(ListView):
    model = Categoria
    template_name = 'core/listar_categoria.html'
    context_object_name = 'categorias'


class NovaCategoriaView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Categoria
    fields = ['nome']
    template_name = 'core/criar_categoria.html'
    success_url = reverse_lazy('listar_categorias')

    permission_required = 'core.add_categoria'
    raise_exception = True


class ExcluirCategoriaView(LoginRequiredMixin, PermissionRequiredMixin, View):
    model = Categoria
    success_url = reverse_lazy('listar_categorias')
    permission_required = 'core.delete_categoria'
    raise_exception = True

    def get(self, request, pk):
        categoria = get_object_or_404(Categoria, pk=pk)
        categoria.delete()
        return redirect(self.success_url)




def listar_mercadorias(request):
    return render(request, "core/listar_mercadorias.html" ) 

# class ListarEstoqueView(ListView):
#     model = Estoque
#     template_name = 'core/listar_mercadorias.html'
#     context_object_name = 'mercadorias'


def criar_mercadoria(request):
    return render(request, "core/criar_mercadoria.html" ) 

def editar_mercadoria(request):
    return render(request, "core/editar_mercadoria.html" ) 

def excluir_mercadoria(request):
    return render(request, "core/excluir_mercadoria.html" ) 



def listar_pessoas(request):
    return render(request, "core/listar_pessoas.html" ) 

def criar_pessoa(request):
    return render(request, "core/criar_pessoa.html" ) 

def editar_pessoa(request):
    return render(request, "core/editar_pessoa.html" ) 

def excluir_pessoa(request):
    return render(request, "core/excluir_pessoa.html" )



def tela_login(request):
    return render(request, "core/login.html" ) 

def tela_estoque(request):
    return render(request, "core/estoque.html" ) 