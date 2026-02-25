from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, View
from django.urls import reverse_lazy
from core.models import Categoria, Estoque, Pessoa


def home(request):
    return render(request, "core/home.html" ) 






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
    success_url = reverse_lazy('listar_categoria')
    permission_required = 'core.delete_categoria'
    raise_exception = True

    def get(self, pk):
        categoria = get_object_or_404(Categoria, pk=pk)
        categoria.delete()
        return redirect(self.success_url)






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

    def get(self, pk):
        estoque = get_object_or_404(Estoque, pk=pk)
        estoque.delete()
        return redirect(self.success_url)






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

    def form_valid(self, form):
        print("FORM VALID ✅")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("FORM INVALID ❌")
        print(form.errors)
        return super().form_invalid(form)


class EditarPessoaView(LoginRequiredMixin, PermissionRequiredMixin, View):
    model = Pessoa
    template_name = 'core/editar_pessoa.html'
    success_url = reverse_lazy('listar_pessoa')
    permission_required = 'core.change_pessoa'
    raise_exception = True

    def get(self, request, pk):
        pessoa = get_object_or_404(Pessoa, pk=pk)
        return render(request, self.template_name, {'pessoa': pessoa})

    def post(self, request, pk):
        pessoa = get_object_or_404(Pessoa, pk=pk)
        pessoa.cpf_cnpj = request.POST.get('cpf_cnpj')
        pessoa.razao_social = request.POST.get('razao_social')
        pessoa.data_nascimento = '2024-01-01' #request.POST.get('data_nascimento')
        pessoa.contato = request.POST.get('contato')
        pessoa.email = request.POST.get('email')
        
       
        pessoa.save()
        return redirect(self.success_url)


class ExcluirPessoasView(LoginRequiredMixin, PermissionRequiredMixin, View):
    model = Pessoa
    success_url = reverse_lazy('listar_pessoa')
    permission_required = 'core.delete_pessoa'
    raise_exception = True

    def get(self, pk):
        pessoa = get_object_or_404(Pessoa, pk=pk)
        pessoa.delete()
        return redirect(self.success_url)



def tela_login(request):
    return render(request, "core/login.html" ) 

def tela_estoque(request):
    return render(request, "core/estoque.html" ) 