from django.shortcuts import redirect, render, get_object_or_404

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.views.generic import CreateView, ListView, DeleteView, UpdateView, View
from django.urls import reverse_lazy

from core.models import Categoria, Estoque

# Create your views here.
def home(request):
    return render(request, "core/home.html" ) 



# def listar_categoria(request):
#     return render(request, "core/listar_categoria.html" ) 
# def criar_categoria(request):
#     return render(request, "core/criar_categoria.html" )
# def editar_categoria(request):
#     return render(request, "core/editar_categoria.html" ) 
# def excluir_categoria(request):
#     return render(request, "core/excluir_categoria.html" )




class ListarCategoriaView(ListView):
    model = Categoria
    template_name = 'core/listar_categoria.html'
    context_object_name = 'categorias'


class NovaCategoriaView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Categoria
    fields = ['nome']
    template_name = 'core/criar_categoria.html'
    success_url = reverse_lazy('listar_categoria')

    permission_required = 'core.add_categoria'
    raise_exception = True


class EditarCategoriaView(LoginRequiredMixin, PermissionRequiredMixin, View):
    model = Categoria
    template_name = 'core/editar_categoria.html'
    success_url = reverse_lazy('listar_categoria')
    permission_required = 'core.change_categoria'
    raise_exception = True

    def get(self, request, pk):
        categoria = get_object_or_404(Categoria, pk=pk)
        return render(request, self.template_name, {'categoria': categoria})

    def post(self, request, pk):
        categoria = get_object_or_404(Categoria, pk=pk)
        categoria.nome = request.POST.get('nome')
        categoria.save()
        return redirect(self.success_url)


class ExcluirCategoriaView(LoginRequiredMixin, PermissionRequiredMixin, View):
    model = Categoria
    ## Caso quiséssemos usar um template para confirmar a exclusão, descomentariamos a linha abaixo e criaríamos o template 'core/confirmar_exclusao_categoria.html'
    # template_name = 'core/confirmar_exclusao_categoria.html'
    success_url = reverse_lazy('listar_categoria')
    permission_required = 'core.delete_categoria'
    raise_exception = True

    # Como não queremos usar um template para confirmar a exclusão, mudamos o mixing para get e não DeleteView
    # Sobrescrevemos o método get para chamar o método post diretamente, assim a exclusão acontece sem precisar de confirmação.
    def get(self, request, pk):
        categoria = get_object_or_404(Categoria, pk=pk)
        categoria.delete()
        return redirect(self.success_url)




# def listar_mercadorias(request):
#     return render(request, "core/listar_mercadorias.html" ) 
# def criar_mercadoria(request):
#     return render(request, "core/criar_mercadoria.html" ) 
# def editar_mercadoria(request):
#     return render(request, "core/editar_mercadoria.html" ) 
# def excluir_mercadoria(request):
#     return render(request, "core/excluir_mercadoria.html" ) 


class ListarEstoqueView(ListView):
    model = Estoque
    template_name = 'core/listar_mercadorias.html'
    context_object_name = 'mercadorias'


class NovoEstoqueView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Estoque
    fields = ['categoria', 'pessoa', 'mercadoria', 'origem', 'saldo']
    template_name = 'core/criar_mercadoria.html'
    success_url = reverse_lazy('listar_mercadoria')

    permission_required = 'core.add_estoque'
    raise_exception = True


class EditarEstoqueView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Estoque
    template_name = 'core/editar_mercadoria.html'
    success_url = reverse_lazy('listar_mercadoria')
    permission_required = 'core.change_estoque'
    raise_exception = True

    def get(self, request, pk):
        estoque = get_object_or_404(Estoque, pk=pk)
        return render(request, self.template_name, {'estoque': estoque})

    def post(self, request, pk):
        estoque = get_object_or_404(Estoque, pk=pk)
        estoque.categoria_id = request.POST.get('categoria')
        estoque.pessoa_id = request.POST.get('pessoa')
        estoque.mercadoria = request.POST.get('mercadoria')
        estoque.origem = request.POST.get('origem')
        estoque.saldo = request.POST.get('saldo')
        estoque.save()
        return redirect(self.success_url)


class ExcluirEstoqueView(LoginRequiredMixin, PermissionRequiredMixin, View):
    model = Estoque
    success_url = reverse_lazy('listar_mercadoria')
    permission_required = 'core.delete_estoque'
    raise_exception = True

    def get(self, request, pk):
        estoque = get_object_or_404(Estoque, pk=pk)
        estoque.delete()
        return redirect(self.success_url)



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