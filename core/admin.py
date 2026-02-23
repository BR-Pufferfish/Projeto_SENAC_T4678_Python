from django.contrib import admin

from core.models import Categoria, Estoque, Movimentacoes, Pessoa

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Pessoa)
admin.site.register(Estoque)
admin.site.register(Movimentacoes)
