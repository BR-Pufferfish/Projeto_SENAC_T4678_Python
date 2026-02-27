from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from core.models import Categoria, Estoque, Movimentacoes, Pessoa






def home(request):
    return render(request, "core/home.html" ) 

def tela_estoque(request):
    return render(request, "core/estoque.html" ) 


class TelaLoginView(LoginView):
    template_name = 'core/login.html'
    redirect_authenticated_user = True



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


class EditarCategoriaView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Categoria
    fields = ['nome']
    template_name = 'core/editar_categoria.html'
    success_url = reverse_lazy('listar_categoria')
    permission_required = 'core.change_categoria'
    raise_exception = True


class ExcluirCategoriaView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Categoria
    success_url = reverse_lazy('listar_categoria')
    permission_required = 'core.delete_categoria'
    raise_exception = True






class ListarEstoqueView(ListView):
    model = Estoque
    template_name = 'core/listar_mercadoria.html'
    context_object_name = 'mercadorias'


class NovoEstoqueView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Estoque
    fields = ['categoria', 'pessoa', 'mercadoria', 'origem', 'saldo']
    template_name = 'core/criar_mercadoria.html'
    success_url = reverse_lazy('listar_mercadoria')

    permission_required = 'core.add_estoque'
    raise_exception = True

    def get(self, request):
        return render(request, self.template_name, {'categorias': Categoria.objects.all(), 'pessoas': Pessoa.objects.all()})


class EditarEstoqueView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Estoque
    fields = ['categoria', 'pessoa', 'mercadoria', 'origem', 'saldo']
    template_name = 'core/editar_mercadoria.html'
    success_url = reverse_lazy('listar_mercadoria')
    permission_required = 'core.change_estoque'
    raise_exception = True


class ExcluirEstoqueView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Estoque
    success_url = reverse_lazy('listar_mercadoria')
    permission_required = 'core.delete_estoque'
    raise_exception = True






class ListarPessoasView(ListView):
    model = Pessoa
    template_name = 'core/listar_pessoa.html'
    context_object_name = 'pessoas'


class CriarPessoasView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Pessoa
    fields = ['cpf_cnpj', 'razao_social', 'data_nascimento', 'contato', 'email', 'tipo_pessoa']
    template_name = 'core/criar_pessoa.html'

      
    success_url = reverse_lazy('listar_pessoa')

    permission_required = 'core.add_pessoa'
    raise_exception = True


class EditarPessoaView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Pessoa
    fields = ['cpf_cnpj', 'razao_social', 'data_nascimento', 'contato', 'email', 'tipo_pessoa'] 
    template_name = 'core/editar_pessoa.html'
    success_url = reverse_lazy('listar_pessoa')
    permission_required = 'core.change_pessoa'
    raise_exception = True


class ExcluirPessoaView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Pessoa
    success_url = reverse_lazy('listar_pessoa')
    permission_required = 'core.delete_pessoa'
    raise_exception = True






class ListarMovimentacaoView(ListView):
    model = Movimentacoes
    template_name = 'core/listar_mercadoria_despachada.html'
    context_object_name = 'movimentacoes'


class FinalizarMovimentacaoView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'core.change_movimentacoes'
    raise_exception = True

    def get(self, request, pk):
        movimentacao = get_object_or_404(Movimentacoes, pk=pk)

        if movimentacao.status == 'Transportando':
            movimentacao.status = 'Entregue'
            movimentacao.save()

        return redirect('listar_mercadoria_despachada')
    

class DespacharView(CreateView):
    model = Movimentacoes
    fields = ['destino']
    template_name = 'core/despachar.html'
    success_url = reverse_lazy('listar_mercadoria_despachada')

    def dispatch(self, request, *args, **kwargs):
        self.estoque = get_object_or_404(Estoque, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estoque'] = self.estoque
        return context

    def form_valid(self, form):
        form.instance.estoque = self.estoque
        form.instance.quantidade = self.estoque.saldo

        self.estoque.status = 'Despachado'
        self.estoque.save()

        return super().form_valid(form)