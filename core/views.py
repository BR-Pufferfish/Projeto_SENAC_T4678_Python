from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "core/home.html" ) 




def listar_categoria(request):
    return render(request, "core/listar_categoria.html" ) 

def criar_categoria(request):
    return render(request, "core/criar_categoria.html" ) 

def editar_categoria(request):
    return render(request, "core/editar_categoria.html" ) 

def excluir_categoria(request):
    return render(request, "core/excluir_categoria.html" ) 



def listar_mercadorias(request):
    return render(request, "core/listar_mercadorias.html" ) 

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